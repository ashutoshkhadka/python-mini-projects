from question_model import Question
from data import question_data, logo
from quiz_brain import QuizBrain


def play_game():
    question_bank = []
    for data in question_data:
        question_bank.append(Question(data["text"], data["answer"]))
    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()


print(logo)
play_game()
print("==================================================================")
print("Thank you for playing 🕹️")
