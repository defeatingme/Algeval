from PySide6.QtWidgets import QDialog
from asm_dialog_ui import Ui_Confirmation
from styles import mboxStyle

from database import Session, AnswerKey
from render_latex import MathJaxSOL


class ASM_Dialog(QDialog):
    def __init__(self, parent, problem, ak_id, has_latex):
        super().__init__(parent)
        self._ui = Ui_Confirmation()  # Initialize the UI
        self._ui.setupUi(self)  # Setup the UI components

        self.problem = problem
        self.answer_key_id = ak_id
        self.has_latex = has_latex

        # Connect buttons to actions
        self._ui.push_allow.clicked.connect(self.allow_asm)
        self._ui.push_forbid.clicked.connect(self.forbid_asm)
        self._ui.push_cancel.clicked.connect(self.reject)  # Close dialog on cancel

        self.user_response = None  # Store user response

        # Set any necessary problem details (like problem number) before showing
        self._ui.label_prob_num.setText(f"Problem {self.problem.problem_number}")
        
        self.fetch_ak_data()


    def fetch_ak_data(self):
        session = Session()
        try:
            answer_key = session.get(AnswerKey, self.answer_key_id)

            ak_content = MathJaxSOL(answer_key.ak_latex)
            has_content = MathJaxSOL(self.has_latex)
        
            # Set LaTeX problem and solution in the web views (if applicable)
            self._ui.web_ak_latex.setHtml(ak_content)  # Set answer key LaTeX
            self._ui.web_has_latex.setHtml(has_content)  # Set student solution LaTeX
            self._ui.label_question.setWordWrap(True)
            self._ui.label_question.setText(self.problem.ask_to_allow_asm)

        except Exception as e:
            mboxStyle.critical(self, "Database Error", f"Failed to retrieve file: {e}")
            print(e)
        finally:
            session.close()


    def allow_asm(self):
        # User allowed the Alternative Solution Method (ASM)
        self.user_response = "Yes, allow it."
        self.accept()  # Close dialog with accept()


    def forbid_asm(self):
        # User forbids the Alternative Solution Method (ASM)
        self.user_response = "No, forbid it."
        self.accept()  # Close dialog with accept()
