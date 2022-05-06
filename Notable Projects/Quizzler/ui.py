from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

# qb = QuizBrain()

class QuizzlerIterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(background=THEME_COLOR, padx=20, pady=20)
        self.windows.minsize(height=500, width=300)

        self.score = Label(text="Score : 0", foreground="white", background=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, background="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=200,
            justify="center",
            text="QUESTION GOES HERE",
            fill=THEME_COLOR,
            font=("airial", 10, "italic"))
        self.canvas.grid(row=1, column=0, pady=50, columnspan=2)

        tick_image = PhotoImage(file="./images/true.png")
        self.tick = Button(image=tick_image, highlightthickness=0, command=self.right_click)
        self.tick.grid(row=2, column=0)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0, command=self.wrong_click)
        self.wrong.grid(row=2, column=1)

        self.next_quiestion()

        self.windows.mainloop()

    def next_quiestion(self):
        self.canvas.config(background="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
        self.score.config(text=f"Score : {self.quiz.score}")

    def right_click(self):
        self.feedback = self.quiz.check_answer(user_answer="true")
        if not self.quiz.still_has_questions():
            exit()
        self.give_feedback(self.feedback)

    def wrong_click(self):
        self.feedback =self.quiz.check_answer(user_answer="false")
        if not self.quiz.still_has_questions():
            exit()
        self.give_feedback(self.feedback)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.windows.after(1000, self.next_quiestion)