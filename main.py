from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
END_TEXT = "You've completed the quiz"


def run_quiz():
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    print(END_TEXT)
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    run_quiz()
