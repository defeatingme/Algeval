from PySide6.QtWidgets import (
    QPushButton, QMessageBox, QTableWidgetItem, QAbstractItemView, QDialog, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from has_dialog_ui import Ui_Table
from styles import buttonStyle, buttonStyle2, mboxStyle, tableStyle

from database import Session, StudentHAS


class HAS_Dialog(QDialog):
    def __init__(self, session_id):
        super().__init__()

        self.session_id = session_id

        self._ui = Ui_Table()
        self._ui.setupUi(self)
        
        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)

        self._ui.table_checked.setStyleSheet(tableStyle)
        self._ui.table_checked.setAlternatingRowColors(True)
        self._ui.table_checked.setSelectionMode(QAbstractItemView.MultiSelection)
        self._ui.table_checked.setSelectionMode(QAbstractItemView.ExtendedSelection) 

        self._ui.push_reload.clicked.connect(self.load_checked)
        self._ui.push_delete_has.clicked.connect(self.delete_selected)

        self._ui.push_back.clicked.connect(self.accept)
    
        self.load_checked()
    

    def load_checked(self):
        session = Session()
        try:
            # Query and sort by Answer Key ID
            student_records = session.query(
                StudentHAS.id,
                StudentHAS.answer_key_id,
                StudentHAS.has_name,
                StudentHAS.sol_fraction,
                StudentHAS.sol_grade,
                StudentHAS.fa_grade,
                StudentHAS.overall_grade,
                StudentHAS.used_asm,
                StudentHAS.has_file,
            ).filter(StudentHAS.session_id == self.session_id).order_by(StudentHAS.answer_key_id.asc()).all()

            row_count = self._ui.table_checked.setRowCount(len(student_records))
            self._ui.table_checked.setColumnCount(8)
            self._ui.table_checked.setHorizontalHeaderLabels([
                "AK ID", "Name", "Solution", "Final Ans.", "Overall", "Used ASM", "Image", "ID"
            ])

            for row, record in enumerate(student_records):
                sol_combined = f"{record.sol_fraction} = {record.sol_grade}"

                # AK ID column
                ak_item = QTableWidgetItem(str(record.answer_key_id))
                ak_item.setTextAlignment(Qt.AlignCenter)
                self._ui.table_checked.setItem(row, 0, ak_item)

                # Student name
                self._ui.table_checked.setItem(row, 1, QTableWidgetItem(record.has_name or "Anonymous"))

                # Solution & grades
                sol_item = QTableWidgetItem((f"{sol_combined}%") or "N/A")
                fa_item = QTableWidgetItem(f"{record.fa_grade}%")
                overall_item = QTableWidgetItem(f"{record.overall_grade}%")

                sol_item.setTextAlignment(Qt.AlignCenter)
                fa_item.setTextAlignment(Qt.AlignCenter)
                overall_item.setTextAlignment(Qt.AlignCenter)

                self._ui.table_checked.setItem(row, 2, sol_item)
                self._ui.table_checked.setItem(row, 3, fa_item)
                self._ui.table_checked.setItem(row, 4, overall_item)

                # Used ASM column
                asm_item = QTableWidgetItem("Yes" if record.used_asm else "No")
                asm_item.setTextAlignment(Qt.AlignCenter)
                self._ui.table_checked.setItem(row, 5, asm_item)

                # Image column
                if record.has_file:
                    pixmap = QPixmap()
                    pixmap.loadFromData(record.has_file)
                    pixmap = pixmap.scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    label = QLabel()
                    label.setPixmap(pixmap)
                    label.setAlignment(Qt.AlignCenter)
                    self._ui.table_checked.setCellWidget(row, 6, label)
                else:
                    self._ui.table_checked.setItem(row, 6, QTableWidgetItem("No Image"))

                # Hidden record ID (useful for reference)
                id_item = QTableWidgetItem(str(record.id))
                id_item.setFlags(Qt.ItemIsEnabled)
                self._ui.table_checked.setItem(row, 7, id_item)

            # Resize, layout, and UX configs
            self._ui.table_checked.resizeColumnsToContents()
            self._ui.table_checked.resizeRowsToContents()
            self._ui.table_checked.horizontalHeader().setStretchLastSection(True)

            total_width = self._ui.table_checked.viewport().width()
            self._ui.table_checked.setColumnWidth(0, int(total_width * 0.05))  # AK ID
            self._ui.table_checked.setColumnWidth(1, int(total_width * 0.25))  # Name
            self._ui.table_checked.setColumnWidth(2, int(total_width * 0.12))  # Solution
            self._ui.table_checked.setColumnWidth(3, int(total_width * 0.10))  # FA
            self._ui.table_checked.setColumnWidth(4, int(total_width * 0.15))  # Overall
            self._ui.table_checked.setColumnWidth(5, int(total_width * 0.10))  # ASM
            self._ui.table_checked.setColumnWidth(6, int(total_width * 0.12))  # Image
            self._ui.table_checked.setColumnHidden(7, True)  # Internal ID
            row_count = self._ui.table_checked.rowCount()
            for row in range(row_count):
                self._ui.table_checked.setRowHeight(row, 128)

            self._ui.table_checked.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            self._ui.table_checked.verticalScrollBar().setSingleStep(5)
            self._ui.table_checked.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self._ui.table_checked.setSelectionBehavior(QAbstractItemView.SelectRows)

            self._ui.label_note.setText(f"{len(student_records)} recorded solution(s).")

        except Exception as e:
            mboxStyle.critical(self, "Database Error", str(e))
            print(e)
        finally:
            session.close()


    def delete_selected(self):
        # Deletes multiple selected checked solutions from the database and removes them from the table
        selected_rows = sorted(set(index.row() for index in self._ui.table_checked.selectionModel().selectedRows()), reverse=True)

        if not selected_rows:
            mboxStyle.warning(self, "No Selection", "Please select at least one checked solution to delete.")
            return

        # Collect checked solution IDs to delete
        has_ids = [int(self._ui.table_checked.item(row, 0).text()) for row in selected_rows]

        # Confirm deletion
        confirmation = mboxStyle.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete {len(has_ids)} selected checked solutions?"
        )

        if confirmation == QMessageBox.No:
            return  # Cancel deletion

        # Delete checked solutions from the database
        session = Session()
        try:
            deleted_has = 0
            deleted_has_name = None

            for has_id in has_ids:
                has_record = session.query(StudentHAS).filter_by(id=has_id).first()
                if has_record:
                    session.delete(has_record)
                    deleted_has += 1
                    
                    if deleted_has == 1:  # Capture ID if only one session is deleted
                        deleted_has_name = has_record.has_name  # Store the name of the deleted record
            
            session.commit()

            # Remove rows from table (from bottom to top to avoid index shift issues)
            for row in selected_rows:
                self._ui.table_checked.removeRow(row)

            if deleted_has == 1:
                self._ui.label_note.setText(f"Solution by {deleted_has_name} has been deleted.")
            else:
                self._ui.label_note.setText(f"{deleted_has} checked solutions have been deleted.")

        except Exception as e:
            session.rollback()
            mboxStyle.critical(self, "Database Error", f"Failed to delete checked solutions: {e}")
            print(f"Error deleting checked solutions: {e}")

        finally:
            session.close()