import tkinter as tk
import random
import time

class MathQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("四則運算-混合版 by 豐哥")
        self.master.geometry("500x600")
        self.start_button = tk.Button(self.master, text="測驗開始", font=("Arial", 52), command=self.start_quiz)
        self.start_button.pack(anchor=tk.CENTER, pady=100)

        self.num_of_questions = 10
        self.label_description = tk.Label(self.master, text=f"說明：\n\n一、本程式會將加減乘除以隨機方式出題\n\n二、總共{self.num_of_questions}題，測驗結束會計算總分及時間", font=("Arial", 12))
        self.label_description.pack(pady=10)

    def start_quiz(self):
        self.start_button.pack_forget()
        self.label_description.forget()
        self.current_question = 1
        self.correct_count = 0
        self.question = tk.StringVar()
        self.user_answer = tk.StringVar()
        self.start_time = time.time()

        self.label_total = tk.Label(self.master, text=f"總共{self.num_of_questions}題，已回答{self.current_question - 1}題", font=("Arial", 12))
        self.label_total.pack(pady=10)

        self.label_question = tk.Label(self.master, textvariable=self.question, font=("Arial", 20))
        self.label_question.pack(pady=20)

        self.entry_answer = tk.Entry(self.master, textvariable=self.user_answer, font=("Arial", 20))
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(self.master, text="提交答案", font=("Arial", 15), command=self.check_answer)
        self.button_submit.pack(pady=10)
        self.master.bind('<Return>', lambda event: self.check_answer())

        self.label_result = tk.Label(self.master, font=("Arial", 20))
        self.label_result.pack(pady=20)
        self.create_buttons()
        self.generate_question()

    def create_buttons(self):  # Number PAD
        # '7', '8', '9'
        self.frame1 = tk.Frame(self.master)
        self.frame1.pack(side=tk.TOP, padx=5, pady=5)
        buttons1 = ['7', '8', '9']
        for button in buttons1:
            btn = tk.Button(self.frame1, text=button, width=5, font=('Arial', 15), command=lambda x=button: self.click(x))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        # '4', '5', '6'
        self.frame2 = tk.Frame(self.master)
        self.frame2.pack(side=tk.TOP, padx=5, pady=5)
        buttons2 = ['4', '5', '6']
        for button in buttons2:
            btn = tk.Button(self.frame2, text=button, width=5, font=('Arial', 15), command=lambda x=button: self.click(x))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        # '1', '2', '3'
        self.frame3 = tk.Frame(self.master)
        self.frame3.pack(side=tk.TOP, padx=5, pady=5)
        buttons3 = ['1', '2', '3']
        for button in buttons3:
            btn = tk.Button(self.frame3, text=button, width=5, font=('Arial', 15), command=lambda x=button: self.click(x))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        # '.', '0', '<-
        self.frame4 = tk.Frame(self.master)
        self.frame4.pack(side=tk.TOP, padx=5, pady=5)
        buttons4 = ['.', '0', '<-']
        for button in buttons4:
            btn = tk.Button(self.frame4, text=button, width=5, font=('Arial', 15), command=lambda x=button: self.click(x))
            btn.pack(side=tk.LEFT, padx=2, pady=2)

        self.restart_button = tk.Button(self.master, text="重新開始", font=("Arial", 20), command=self.restart_quiz)
        self.restart_button.pack(anchor=tk.CENTER, pady=10)

    def restart_quiz(self): #重新開始
        self.entry_answer.delete(0, tk.END)
        self.label_result.pack_forget()
        self.label_total.pack_forget()
        self.label_question.pack_forget()
        self.entry_answer.pack_forget()
        self.button_submit.pack_forget()
        self.restart_button.pack_forget()
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.__init__(self.master)

    def click(self, key):
        if key == '<-':
            self.user_answer.set(self.user_answer.get()[:-1])
        else:
            self.user_answer.set(self.user_answer.get() + key)

    def generate_question(self):
        operators = ['+', '-', 'x', '÷']
        operator = random.choice(operators)
        if operator == '+':
            num1 = random.randint(2, 100)
            num2 = random.randint(2, 100)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 + num2
        elif operator == '-':
            num1 = random.randint(10, 100)
            num2 = random.randint(2, num1-1)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 - num2
        elif operator == 'x':
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 * num2
        elif operator == '÷':
            num2 = random.randint(2, 10)
            num1 = num2 * random.randint(2, 10)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 // num2

    def check_answer(self):
        try:
            user_answer = int(self.user_answer.get())
            if user_answer == self.answer:
                self.label_result.config(text="答案正確！", fg="green")
                self.correct_count += 1
            else:
                self.label_result.config(text=f"答案錯誤！正確答案是{self.answer}", fg="red")
            self.current_question += 1
            self.label_total.config(text=f"總共{self.num_of_questions}題，已回答{self.current_question - 1}題")
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
        message = f"遊戲結束！你的得分是{score}分\n總共使用{total_time}秒"
        self.entry_answer.pack_forget()
        self.button_submit.pack_forget()
        self.label_result.config(text=message, fg="blue")
        self.button_submit.config(state="disabled")

root = tk.Tk()
app = MathQuiz(root)
root.mainloop()