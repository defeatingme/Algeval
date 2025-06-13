from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from ak_dialog_ui import Ui_Dialog
from styles import mboxStyle

from database import Session, AnswerKey
from render_latex import MathJaxSOL


class AK_Dialog(QDialog):
    def __init__(self, session_id):
        super().__init__()

        self.session_id = session_id

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
    
        self.fetch_ak_data()
        
        self._ui.push_back.clicked.connect(self.accept)


    def fetch_ak_data(self):
        # Initialize pixmap
        pixmap = None

        # Retrieves and displays the saved answer key file in a QLabel
        session = Session()
        try:
            # Fetch the first two answer_key records associated with the session_id
            answer_keys = session.query(
                AnswerKey.fa_weight, 
                AnswerKey.steps_count, 
                AnswerKey.ak_latex,
                AnswerKey.ak_file
                ) \
                .filter_by(session_id=self.session_id) \
                .order_by(AnswerKey.created_at.asc()) \
                .limit(2) \
                .all()

            # Display first answer key if available
            if len(answer_keys) >= 1:
                print(f"First answer key ={answer_keys[0].ak_latex}, FA Weight={answer_keys[0].fa_weight}, Steps={answer_keys[0].steps_count}")
                
                # Process first answer key
                ak1 = answer_keys[0]
                
                # Set text labels for first answer key
                self._ui.label_sol_steps.setText(f"Solution steps: {ak1.steps_count}")
                self._ui.label_fa_grade.setText(f"Final answer weight: {ak1.fa_weight}%")
                
                # Process and display LaTeX content
                if ak1.ak_latex:
                    html_content = MathJaxSOL(ak1.ak_latex)
                    self._ui.web_latex.setHtml(html_content)
                
                # Process and display image
                if ak1.ak_file:
                    file = QImage.fromData(ak1.ak_file)
                    if not file.isNull():
                        pixmap = QPixmap.fromImage(file)
                        self._ui.label_file.setPixmap(pixmap.scaled(420, 420, Qt.AspectRatioMode.KeepAspectRatio))
                    else:
                        print("First answer key image data is invalid")
            
            # Display second answer key if available
            if len(answer_keys) >= 2:
                print(f"Second answer key={answer_keys[1].ak_latex}, FA Weight={answer_keys[1].fa_weight}, Steps={answer_keys[1].steps_count}")
                
                # Process second answer key
                ak2 = answer_keys[1]
                
                # Set text labels for second answer key
                self._ui.label_sol_steps_2.setText(f"Solution steps: {ak2.steps_count}")
                self._ui.label_fa_grade_2.setText(f"Final answer weight: {ak2.fa_weight}%")
                
                # Process and display LaTeX content
                if ak2.ak_latex:
                    html_content_2 = MathJaxSOL(ak2.ak_latex)
                    self._ui.web_latex_2.setHtml(html_content_2)
                
                # Process and display image
                if ak2.ak_file:
                    file = QImage.fromData(ak2.ak_file)
                    if not file.isNull():
                        pixmap = QPixmap.fromImage(file)
                        self._ui.label_file_2.setPixmap(pixmap.scaled(420, 420, Qt.AspectRatioMode.KeepAspectRatio))
                    else:
                        print("Second answer key image data is invalid")
            
            # Adjust UI based on number of answer keys
            if len(answer_keys) < 2:
                self.resize(800, 540)
                self.setFixedSize(800, 540)
                self._ui.push_back.setGeometry(550, 500, 241, 25)
            else:
                self._ui.push_back.setGeometry(680, 500, 241, 25)

                
        except Exception as e:
            print(f"Error fetching answer key data: {e}")
            mboxStyle.warning(self, "Database Error", f"Error retrieving answer key data: {str(e)}")
        finally:
            session.close()