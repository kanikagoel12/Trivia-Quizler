import tkinter as tk
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20)
        self.window.configure(background=THEME_COLOR)
        self.score_label = tk.Label(text=f"Score: {self.quiz.score}",fg="white",bg=THEME_COLOR,font=("Arial",20))
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="Some Question text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2,column=0)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image,highlightthickness=0,command=self.false)
        self.false_button.grid(row=2,column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            q_text = html.unescape(q_text)
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.true_button.config(state=tk.DISABLED)
            self.false_button.config(state=tk.DISABLED)

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,answer):
        if answer == "True":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.configure(text=f"Score: {self.quiz.score}")
        self.window.after(500, self.reset)

    def reset(self):
        self.canvas.config(background=THEME_COLOR)
        self.get_next_question()