from tkinter import *

THEME_COLOR = "#375362"
FONT = ("ariel", 20, "italic")
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="", width=250, font=FONT)

        false_image = PhotoImage(file="./images/false.png")
        true_image = PhotoImage(file="./images/true.png")

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.wrong_button = Button(image=false_image, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)

        self.right_button = Button(image=true_image, highlightthickness=0)
        self.right_button.grid(column=0, row=2, padx=20, pady=20)
        self.get_next()

        self.window.mainloop()

    def get_next(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
