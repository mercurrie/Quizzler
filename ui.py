from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
PAD_X = 20
PAD_Y = 20
WINDOW_TITLE = "Quizzler"
LABEL_FG_COLOR = "White"
SCORE_LABEL_ROW = 0
SCORE_LABEL_COLUMN = 1
SCORE_LABEL_TEXT = "Score: 0/10"
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
CANVAS_COLOR = "White"
CANVAS_ROW = 1
CANVAS_COLUMN = 0
CANVAS_COLUMN_SPAN = 2
CANVAS_PAD_Y = 50
FALSE_IMG = "images/false.png"
FALSE_IMG_ROW = 2
FALSE_IMG_COLUMN = 1
FALSE_IMG_HIGHLIGHT = 0
TRUE_IMG = "images/true.png"
TRUE_IMG_ROW = 2
TRUE_IMG_COLUMN = 0
TRUE_IMG_HIGHLIGHT = 0
QUESTION_TEXT_X = 150
QUESTION_TEXT_Y = 125
QUESTION_WIDTH = 280
QUESTION_FONT = ("Arial", 20, "italic")
QUIZ_END_TEXT = "You've reached the end of the quiz."
WRONG_ANS_CLR = "red"
RIGHT_ANS_CLR = "green"
WINDOW_DELAY = 1000


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(WINDOW_TITLE)
        self.window.config(padx=PAD_Y, pady=PAD_Y, bg=THEME_COLOR)

        self.score_label = Label(text=SCORE_LABEL_TEXT, fg=LABEL_FG_COLOR, bg=THEME_COLOR)
        self.score_label.grid(row=SCORE_LABEL_ROW, column=SCORE_LABEL_COLUMN)

        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=CANVAS_COLOR)
        self.question_text = self.canvas.create_text(
            QUESTION_TEXT_X,
            QUESTION_TEXT_Y,
            width=QUESTION_WIDTH,
            text="",
            fill=THEME_COLOR,
            font=QUESTION_FONT)
        self.canvas.grid(row=CANVAS_ROW, column=CANVAS_COLUMN, columnspan=CANVAS_COLUMN_SPAN, pady=CANVAS_PAD_Y)

        true_img = PhotoImage(file=TRUE_IMG)
        self.true_button = Button(image=true_img, highlightthickness=TRUE_IMG_HIGHLIGHT, command=self.true_pressed)
        self.true_button.grid(row=TRUE_IMG_ROW, column=TRUE_IMG_COLUMN)

        false_img = PhotoImage(file=FALSE_IMG)
        self.false_button = Button(image=false_img, highlightthickness=FALSE_IMG_HIGHLIGHT, command=self.false_pressed)
        self.false_button.grid(row=FALSE_IMG_ROW, column=FALSE_IMG_COLUMN)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        self.score_label.config(text=f"score: {self.quiz.score}/10")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=QUIZ_END_TEXT)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg=RIGHT_ANS_CLR)
        else:
            self.canvas.config(bg=WRONG_ANS_CLR)

        self.window.after(WINDOW_DELAY, self.get_next_question)
