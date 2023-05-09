import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="score: 1", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300,
                             height=250,
                             bg=THEME_COLOR,
                             highlightthickness=0)
        self.question_canvas = self.canvas.create_text(
            150,
            125,
            width=280,
            text="your question goes here",
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image,
                                  highlightbackground=THEME_COLOR,
                                  command=self.check_true)
        self.true_button.grid(row=2, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image,
                                   highlightbackground=THEME_COLOR,
                                   command=self.check_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.itemconfig(self.question_canvas, text=self.quiz.next_question())

    def check_true(self):
        result = self.quiz.check_answer("true")
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        time.sleep(1)
        self.get_next_ques()

    def check_false(self):
        result = self.quiz.check_answer("false")
        if result:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")
        time.sleep(1)
        self.get_next_ques()
