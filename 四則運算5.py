import tkinter as tk
import random
import time

class MathQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("小學四則運算練習")
        self.master.geometry("500x300")
        self.num_of_questions = 10
        self.current_question = 1
        self.correct_count = 0
        self.question = tk.StringVar()
        self.user_answer = tk.StringVar()
        self.start_time = time.time()

        self.label_total = tk.Label(self.master, text=f"總共{self.num_of_questions}題", font=("Arial", 12))
        self.label_total.pack(pady=10)

        self.label_question_count = tk.Label(self.master, text=f"已回答{self.current_question - 1}題", font=("Arial", 12))
        self.label_question_count.pack(pady=10)

        self.label_question = tk.Label(self.master, textvariable=self.question, font=("Arial", 20))
        self.label_question.pack(pady=20)

        self.entry_answer = tk.Entry(self.master, textvariable=self.user_answer, font=("Arial", 20))
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(self.master, text="提交答案", command=self.check_answer)
        self.button_submit.pack(pady=10)
        self.master.bind('<Return>', lambda event: self.check_answer())

        self.label_result = tk.Label(self.master, font=("Arial", 20))
        self.label_result.pack(pady=20)

        self.generate_question()

    def generate_question(self):
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        if operator == '/':
            num2 = random.randint(2, 10)
            num1 = num2 * random.randint(2, 10)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 // num2
        elif operator == '-':
            num1 = random.randint(10, 100)
            num2 = random.randint(1, num1-1)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 - num2
        elif operator == '*':
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 * num2
        elif operator == '+':
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 + num2


    def check_answer(self):
        try:
            user_answer = int(self.user_answer.get())
            if user_answer == self.answer:
                self.label_result.config(text="答案正確！", fg="green")
                self.correct_count += 1
            else:
                self.label_result.config(text=f"答案錯誤！正確答案是{self.answer}", fg="red")
            self.current_question += 1
            self.label_question_count.config(text=f"已回答{self.current_question - 1}題")
            if self.current_question > self.num_of_questions:
                self.end_quiz()
            else:
                self.generate_question()
                self.user_answer.set('')
        except ValueError:
            self.label_result.config(text="請輸入數字！", fg="red")

    def end_quiz(self):
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        score = round(self.correct_count / self.num_of_questions * 100)
        self.entry_answer.pack_forget()
        self.button_submit.pack_forget()
        message = f"遊戲結束！你的得分是{score}分\n總共使用{total_time}秒"
        self.label_result.config(text=message, fg="blue")
        self.button_submit.config(state="disabled")

root = tk.Tk()
app = MathQuiz(root)
root.mainloop()