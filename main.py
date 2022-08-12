from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q_text=question["question"], q_answer=question["correct_answer"]) for question in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{quiz.question_number}")
