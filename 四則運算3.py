import random
import tkinter as tk

class MathQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("小學四則運算練習")
        self.master.geometry("400x400")

        self.num_of_questions = 2
        self.current_question = 1
        self.correct_count = 0
        self.question = tk.StringVar()
        self.user_answer = tk.StringVar()

        self.label_question = tk.Label(self.master, textvariable=self.question, font=("Arial", 20))
        self.label_question.pack(pady=20)

        self.entry_answer = tk.Entry(self.master, textvariable=self.user_answer, font=("Arial", 20))
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(self.master, text="提交答案", command=self.check_answer)
        self.button_submit.pack(pady=10)

        self.label_result = tk.Label(self.master, font=("Arial", 20))
        self.label_result.pack(pady=20)

        self.generate_question()

    def generate_question(self):
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        if operator == '/':
            num2 = random.randint(1, 10)
            num1 = num2 * random.randint(1, 10)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 // num2
        elif operator == '-':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, num1)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 - num2
        elif operator == '*':
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            self.question.set(f"{num1} {operator} {num2} = ")
            self.answer = num1 * num2
        else:
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
            if self.current_question > self.num_of_questions:
                self.show_score()
            else:
                self.generate_question()
        except ValueError:
            self.label_result.config(text="輸入無效！", fg="red")

    def show_score(self):
        score = self.correct_count / self.num_of_questions * 100
        message = f"總共{self.num_of_questions}題，答對{self.correct_count}題，得分{score:.2f}%"
        self.label_question.config(text=message)
        self.entry_answer.destroy()
        self.button_submit.destroy()
        self.label_result.destroy()

def main():
    root = tk.Tk()
    quiz = MathQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
