import tkinter
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("ariel", 20, "italic")


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

        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.res_right)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)

        self.right_button = Button(image=true_image, highlightthickness=0, command=self.res_wrong)
        self.right_button.grid(column=0, row=2, padx=20, pady=20)
        self.get_next()

        self.window.mainloop()

    def res_right(self):
        q_res = self.quiz.check_answer("True")
        self.get_feedback(q_res)

    def res_wrong(self):
        q_res = self.quiz.check_answer("False")
        self.get_feedback(q_res)

    def get_feedback(self, feedback):
        if feedback is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next)

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score is {self.quiz.score}/10")
            self.right_button.config(command=DISABLED)
            self.wrong_button.config(command=DISABLED)
