import time
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Qt, Signal

from rec_dialog_ui import Ui_Dialog
from styles import buttonStyle, buttonStyle2, mboxStyle

from database import Session, AnswerKey
from recommend import Recommendation
from ak_dialog import AK_Dialog
from render_latex import MathJaxSOL, ClearHTML


class Rec_Dialog(QWidget):
    asmProcessed = Signal(int, str, str)

    def __init__(self, session_window, session_id, ak_id):
        super().__init__()

        self.session_window = session_window
        self.session_id = session_id
        self.ak_id = ak_id
        self.ak_latex = None
        self.steps_count = None
        
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)
        self._ui.push_generate.setStyleSheet(buttonStyle2)

        self.clearhtml = ClearHTML()
        self._ui.web_latex.setHtml(self.clearhtml)

        self.asm_latex = None

        self._ui.push_generate.clicked.connect(self.generateRec)
        self._ui.push_allow.clicked.connect(self.allow_asm)
        self._ui.push_forbid.clicked.connect(self.forbid_asm)
        self._ui.push_view.clicked.connect(self.view_ak_data)
        self._ui.push_cancel.clicked.connect(self.backToSession)

        self._ui.push_allow.setEnabled(False)
        self._ui.push_forbid.setEnabled(False)
        
        self.fetchAnswerKey()


    def fetchAnswerKey(self):
        session = Session()  # Open a new session
        try:
            # Query all AnswerKey entries linked to the session_id
            answer_key = session.get(AnswerKey, self.ak_id)

            if answer_key is None:
                raise ValueError(f"AnswerKey with ID {self.ak_id} not found!")
            self.ak_latex = answer_key.ak_latex
            self.steps_count = answer_key.steps_count if answer_key.steps_count else "Unspecified"
            
            self.rec = Recommendation(self.ak_latex, self.steps_count)

        except Exception as e:
            print(e)
            mboxStyle.warning(self, "Database Error", str(e))
            self.reject()  # Close the dialog safely

        finally:
            session.close()  # Close the session


    def generateRec(self):
        self._ui.push_generate.setEnabled(False)
        self._ui.push_allow.setEnabled(False)
        self._ui.push_forbid.setEnabled(False)

        start_total_timer = time.time()

        request = self._ui.edit_asm.toPlainText().strip() or "Recommend an alternative solution method differing from the answer key I provided..."
        try:
            self.asm_result = self.rec.recommend(request)
            if self.asm_result.refusal:
                raise Exception(self.asm_result.refusal)
            else:
                self.asm_result = self.asm_result.parsed
                self.asm_latex = self.asm_result.alternative_solution
                self.asm_steps = self.asm_result.steps_count

                self._ui.label_steps.setText(f"No. of steps: {self.asm_steps}")
                html_content = MathJaxSOL(self.asm_latex)
                self._ui.web_latex.setHtml(html_content)

                runtime = time.time() - start_total_timer

        except Exception as e:
            runtime = time.time() - start_total_timer
            mboxStyle.warning(self, "ASM Error", str(e))
            print(e)

        finally:
            self._ui.label_time.setText(f"Runtime: {runtime: .2f}s")
            self._ui.push_generate.setEnabled(True)
            self._ui.push_allow.setEnabled(True)
            self._ui.push_forbid.setEnabled(True)


    def allow_asm(self):
        # User allowed ASM
        self.asm_choice = "Allow ASM for HAS"
        self.submitASM()  # Close dialog with accept()


    def forbid_asm(self):
        # User forbid ASM
        self.asm_choice = "Forbid ASM for HAS"
        self.submitASM()


    def submitASM(self):
        self.asmProcessed.emit(self.asm_steps, self.asm_latex, self.asm_choice)
        self.close()


    def view_ak_data(self):
        if self.ak_latex == None:
            mboxStyle.warning(self, "Warning", "Please input and save an answer key data first.")
            return

        dialog = AK_Dialog(self.session_id)
        dialog.exec()  # Opens the dialog modally (blocks input to main window)


    def backToSession(self):
        self.close()


    def closeEvent(self, event):
        self.session_window.setEnabled(True)
        event.accept()