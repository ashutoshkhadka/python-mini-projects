class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number + 1} {question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(answer, question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            print("You got it right! 👍")
            self.score += 1
        else:
            print("Sorry, wrong answer. 😭")
        print(f"Your score: {self.score}/ {self.question_number}")
