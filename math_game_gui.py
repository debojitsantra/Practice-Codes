import tkinter as tk
from tkinter import messagebox
import random

class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game")
        self.level = 1
        self.k = 1
        self.j = 100

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.status_label = tk.Label(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.next_button = tk.Button(root, text="Next Level", command=self.next_level, state="disabled")
        self.next_button.pack(pady=5)

        self.new_question()

    def new_question(self):
        self.n1 = random.randint(self.k, self.j)
        self.n2 = random.randint(self.k, self.j)
        self.question_label.config(text=f"Level {self.level}: {self.n1} + {self.n2}")
        self.answer_entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.next_button.config(state="disabled")

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.n1 + self.n2:
                self.status_label.config(text="Right!!")
                self.next_button.config(state="normal")
            else:
                messagebox.showerror("Wrong!", "Game Over!")
                self.root.destroy()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def next_level(self):
        proceed = messagebox.askyesno("Continue?", "Do you want to proceed to another level?")
        if proceed:
            self.level += 1
            self.k = self.j
            self.j = self.j + 100 * self.level
            self.new_question()
        else:
            self.root.destroy()

root = tk.Tk()
game = MathGame(root)
root.mainloop()