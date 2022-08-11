from data import question_data
from question_model import Question

question_bank = [Question(q_text=question["text"], q_answer=question["answer"]) for question in question_data]
