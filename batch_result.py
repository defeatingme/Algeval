from __future__ import annotations
from pathlib import Path
import json
import textwrap

from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from batch_result_ui import Ui_Result
from styles import buttonStyle, buttonStyle2, mboxStyle, gradeLabelStyle

from eval_batch import AssistantResponse, ProblemResponse, SolutionGrade
from render_latex import MathJaxSOL, MathJaxRes
from database import Session, AnswerKey, StudentHAS
from ak_dialog import AK_Dialog


class Batch_Result(QWidget):        
    def __init__(self, batch_window, session_id, ocr_result, gpt_result):
        super().__init__()

        self.batch_window = batch_window
        self.session_id = session_id
        self.ocr_result = ocr_result
        self.gpt_result = gpt_result
        self.page = 0
        
        # Attribute from AnswerKey table 
        self.first_ak_id = None
        self.second_ak_id = None
        self.answer_key_ids = []

        self._ui = Ui_Result()
        self._ui.setupUi(self)

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)
        self._ui.push_save.setStyleSheet(buttonStyle2)

        self._ui.push_prev.clicked.connect(self.prev_page)
        self._ui.push_next.clicked.connect(self.next_page)
        self._ui.push_save.clicked.connect(self.save_to_database)
        self._ui.push_cancel.clicked.connect(self.go_back)
        self.display_results()

        self.fetchStats()

        
    def display_results(self):            
        self.display_page()

        pixmap = QPixmap(self.ocr_result[self.page]['has_file'])
        self._ui.label_image.setPixmap(pixmap.scaled(270, 270, Qt.AspectRatioMode.KeepAspectRatio))

        has_name = self.ocr_result[self.page]['result'].get('name')
        if (not has_name) or (has_name == 'null'):
            has_name = 'Anonymous'
        self._ui.edit_student_name.setText(has_name)

        has_latex = self.gpt_result[self.page]['has_latex']
        html_content = MathJaxSOL(has_latex)
        self._ui.web_latex.setHtml(html_content)

        result_data = json.loads(self.gpt_result[self.page].get('gpt_response'))
        try:
            # Reconstruct problems
            problems = []
            if result_data.get('problems'):
                for p_data in result_data['problems']:
                    # Reconstruct sol_calculation
                    sol_calculation = []
                    if p_data.get('sol_calculation'):
                        for s_data in p_data['sol_calculation']:
                            sol_grade = SolutionGrade(**s_data)
                            sol_calculation.append(sol_grade)
                    
                    # Create ProblemResponse
                    problem = ProblemResponse(
                        problem_number=p_data['problem_number'],
                        problem=p_data['problem'],
                        ask_to_allow_asm=p_data.get('ask_to_allow_asm'),
                        steps_and_result=p_data.get('steps_and_result'),
                        employed_asm=p_data.get('employed_asm', False),
                        sol_calculation=sol_calculation,
                        fa_grade=p_data.get('fa_grade'),
                        overall_grade=p_data.get('overall_grade')
                    )
                    problems.append(problem)
            
            # Create AssistantResponse
            self.result_obj = AssistantResponse(
                problems=problems,
                no_HAS_message=result_data.get('no_HAS_message')
            )
            
            if self.result_obj.problems:
                self.display_eval()
            else:
                html_content = MathJaxRes(self.result_obj.no_HAS_message)
                self._ui.web_result.setHtml(html_content)
                
        except Exception as e:
            mboxStyle.warning(self, "Display Error", str(e))
            print(f"Failed to parse result string: {e}")

        print(":33")


    def display_eval(self):
        result_display = "\n\n---\n\n".join(
            textwrap.dedent(f"""\
            ### Problem {prob.problem_number}. {prob.problem}\n{prob.result}\n
            Solution = ({prob.sol_calculation[0].correct_steps}/{prob.sol_calculation[0].total_steps}){prob.sol_calculation[0].weight} = {prob.sol_calculation[0].sol_grade}%
            Final Answer = {prob.fa_grade}%
            Overall Score = {prob.overall_grade}%
            """)
            if prob.sol_calculation else
            textwrap.dedent(f"""\
            ### Problem {prob.problem_number}. {prob.problem}\n{prob.result}\n
            Solution = None = 0%
            Final Answer = {prob.fa_grade or 0}%
            Overall Score = {prob.overall_grade or 0}%
            """)

            for prob in self.result_obj.problems
            ) 

        html_content = MathJaxRes(str(fr'{result_display}'))
        self._ui.web_result.setHtml(html_content)
        # First problem
        if len(self.result_obj.problems) > 0:
            prob_1 = self.result_obj.problems[0]
            self._ui.label_prob_grade.setText(f"Grade for Problem {prob_1.problem_number}:")
            if prob_1.sol_calculation:
                self._ui.label_sol_grade.setText(f"Solution:\n({prob_1.sol_calculation[0].correct_steps}/{prob_1.sol_calculation[0].total_steps}){prob_1.sol_calculation[0].weight} = {prob_1.sol_calculation[0].sol_grade}%")
            else:
                self._ui.label_sol_grade.setText(f"Solution:\nNone = 0%")
            self._ui.label_fa_grade.setText(f"Final Answer:\n{prob_1.fa_grade}%")
            self._ui.label_overall_grade.setText(f"Overall:\n{prob_1.overall_grade}%")

        # Second problem (if exists)
        if len(self.result_obj.problems) > 1:
            prob_2 = self.result_obj.problems[1]
            self._ui.label_prob_grade_2.setText(f"Grade for Problem {prob_2.problem_number}:")
            if prob_2.sol_calculation:
                self._ui.label_sol_grade_2.setText(f"Solution:\n({prob_2.sol_calculation[0].correct_steps}/{prob_2.sol_calculation[0].total_steps}){prob_2.sol_calculation[0].weight} = {prob_2.sol_calculation[0].sol_grade}%")
            else:
                self._ui.label_sol_grade_2.setText(f"Solution:\nNone = 0%")
            self._ui.label_fa_grade_2.setText(f"Final Answer:\n{prob_2.fa_grade}%")
            self._ui.label_overall_grade_2.setText(f"Overall:\n{prob_2.overall_grade}%")

            self._ui.label_prob_grade_2.setStyleSheet(gradeLabelStyle)
            self._ui.label_sol_grade_2.setStyleSheet(gradeLabelStyle)
            self._ui.label_fa_grade_2.setStyleSheet(gradeLabelStyle)
            self._ui.label_overall_grade_2.setStyleSheet(gradeLabelStyle)


    def display_page(self):
        self._ui.label_page.setText(f"Page {self.page + 1} of {len(self.ocr_result)}")
    
 
    ################################################################################
    # Save and Close window

    def save_to_database(self):
        self._ui.push_save.setEnabled(False)

        for i, result in enumerate(self.gpt_result):
            has_name = self.ocr_result[i]['result'].get('name')
            if (not has_name) or (has_name == 'null'):
                has_name = 'Anonymous'
            self._ui.edit_student_name.setText(has_name)

            has_latex = result['has_latex']

            # Validate the file path before reading the file
            filename = self.ocr_result[i]['has_file']
            if filename == None:
                if self.has_file == None:
                    mboxStyle.warning(self, "Error", "No file selected. Please upload an answer key file.");
                    return
                else:
                    pass
            else:
                # Read file
                try:
                    with open(filename, "rb") as file:
                        self.has_file = file.read()
                except FileNotFoundError:
                    mboxStyle.critical(self, "Error", "File not found. Please check the file path.")
                    return
            
            result_data = json.loads(self.gpt_result[self.page].get('gpt_response'))
            try:
                # Reconstruct problems
                problems = []
                if result_data.get('problems'):
                    for p_data in result_data['problems']:
                        # Reconstruct sol_calculation
                        sol_calculation = []
                        if p_data.get('sol_calculation'):
                            for s_data in p_data['sol_calculation']:
                                sol_grade = SolutionGrade(**s_data)
                                sol_calculation.append(sol_grade)
                        
                        # Create ProblemResponse
                        problem = ProblemResponse(
                            problem_number=p_data['problem_number'],
                            problem=p_data['problem'],
                            ask_to_allow_asm=p_data.get('ask_to_allow_asm'),
                            steps_and_result=p_data.get('steps_and_result'),
                            employed_asm=p_data.get('employed_asm', False),
                            sol_calculation=sol_calculation,
                            fa_grade=p_data.get('fa_grade'),
                            overall_grade=p_data.get('overall_grade')
                        )
                        problems.append(problem)
                
                # Create AssistantResponse
                self.result_obj = AssistantResponse(
                    problems=problems,
                    no_HAS_message=result_data.get('no_HAS_message')
                )
                
                if self.result_obj.problems:
                    self.display_eval()
                else:
                    html_content = MathJaxRes(self.result_obj.no_HAS_message)
                    self._ui.web_result.setHtml(html_content)
                    
            except Exception as e:
                mboxStyle.warning(self, "Display Error", str(e))
                print(f"Failed to parse result string: {e}")

            print(":33")
            
            prob_result = self.result_obj.problems
            # Modified code to save results for multiple problems

            if len(prob_result) > 1:
                # If we have two problems to save
                session = Session()
                try:
                    for i, prob in enumerate(prob_result[:2]):  # Iterate over list properly
                        for j, ak_id in enumerate(self.answer_key_ids):
                            if prob.problem_number == (j+1):
                                answer_key_id = ak_id
                                break

                        # Extract values safely for each problem
                        result = prob.result
                        employed_asm = prob.employed_asm or False
                                    
                        if prob.sol_calculation:
                            sol_fraction = f"{prob.sol_calculation[0].correct_steps}/{prob.sol_calculation[0].total_steps}"
                            sol_grade = prob.sol_calculation[0].sol_grade
                        else:
                            sol_fraction = None
                            sol_grade = 0

                        fa_grade = prob.fa_grade or 0
                        overall_grade = prob.overall_grade or 0


                        # Create a new StudentHAS entry for each problem
                        student_has = StudentHAS(
                            session_id=self.session_id,
                            answer_key_id=answer_key_id,
                            has_name=has_name,
                            has_latex=has_latex,
                            result=result,
                            sol_fraction=sol_fraction,
                            sol_grade=sol_grade,
                            fa_grade=fa_grade,
                            overall_grade=overall_grade,
                            used_asm=employed_asm,
                            has_file=self.has_file
                        )

                        # Add each entry
                        session.add(student_has)
                    
                    # Commit all entries at once
                    session.commit()

                    # Update UI elements
                    self.counter = session.query(StudentHAS).filter_by(session_id=self.session_id).count()
                    #UI notifs
                    self._ui.edit_student_name.setText("")

                except Exception as e:
                    # Rollback session if error occurs
                    session.rollback()
                    mboxStyle.critical(self, "Database Error", f"Error saving StudentHAS: {str(e)}")
                    self._ui.push_save.setEnabled(True)
                    print(e)
                finally:
                    # Close the session
                    session.close()

            elif len(prob_result) == 1:
                for j, ak_id in enumerate(self.answer_key_ids):
                    if prob_result[0].problem_number == (j+1):
                        answer_key_id = ak_id
                        break

                session = Session()
                try:
                    # Extract values safely
                    result = prob_result[0].result
                    employed_asm = prob_result[0].employed_asm or False
                                
                    if prob_result[0].sol_calculation:
                        sol_fraction = f"{prob_result[0].sol_calculation[0].correct_steps}/{prob_result[0].sol_calculation[0].total_steps}"
                        sol_grade = prob_result[0].sol_calculation[0].sol_grade
                    else:
                        sol_fraction = None
                        sol_grade = 0

                    fa_grade = prob_result[0].fa_grade or 0
                    overall_grade = prob_result[0].overall_grade or 0

                    
                    # Create a new StudentHAS entry
                    student_has = StudentHAS(
                        session_id=self.session_id,
                        answer_key_id=answer_key_id,
                        has_name=has_name,
                        has_latex=has_latex,
                        result=result,
                        sol_fraction=sol_fraction,
                        sol_grade=sol_grade,
                        fa_grade=fa_grade,
                        overall_grade=overall_grade,
                        used_asm=employed_asm,
                        has_file=self.has_file
                    )
                    # Add each entry
                    session.add(student_has)
                    
                    # Commit all entries at once
                    session.commit()

                    self.counter = session.query(StudentHAS).filter_by(session_id=self.session_id).count()
                    #UI notifs
                    self._ui.edit_student_name.setText("")

                except Exception as e:
                    # Rollback session if error occurs
                    session.rollback()
                    mboxStyle.critical(self, "Database Error", f" Error saving StudentHAS: {str(e)}")
                    self._ui.push_save.setEnabled(True)
                    print(e)
                finally:
                    # Close the session
                    session.close()
            else:
                print("No HAS. Skipping...")
                continue


    def fetchStats(self):
        session = Session()
        try:
            # Fetch the first two answer_key records associated with the session_id
            answer_keys = session.query(AnswerKey.id, AnswerKey.fa_weight, AnswerKey.steps_count) \
                .filter_by(session_id=self.session_id) \
                .order_by(AnswerKey.created_at.asc()) \
                .limit(2) \
                .all()

            # Extract values or set defaults if fewer than 2 exist
            if len(answer_keys) >= 1:
                self.first_ak_id = answer_keys[0].id
                self.answer_key_ids.append(self.first_ak_id)

            else:
                self.first_ak_id = "None"

            if len(answer_keys) >= 2:
                self.second_ak_id = answer_keys[1].id
                self.answer_key_ids.append(self.second_ak_id)
            else:
                self.second_ak_id = "None"
                
        except Exception as e:
            mboxStyle.critical(self, "Database Error", f"Error fetching AK data: {str(e)}")
            print(f"Error fetching AK data: {e}")

        finally:
            session.close()


    def next_page(self):
        self.page += 1
        if self.page > len(self.ocr_result) - 1:
            self.page -= 1
        self.display_results()

        
    def prev_page(self):
        self.page -= 1
        if self.page < 0:
            self.page = 0
        self.display_results()

        
    def go_back(self):
        self.close()
        self.batch_window.show()


    ################################################################################
    # Miscellaneous

    def viewAnswerKey(self):
        dialog = AK_Dialog(self.session_id)
        dialog.exec()  # Opens the dialog modally (blocks input to main window)