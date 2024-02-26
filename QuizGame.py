import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("NDA Exam Quiz Game")
        self.root.geometry("600x400")
        
        self.questions = [
            {
                "question": "Who is the current Chief of Army Staff of India?",
                "options": ["General Bipin Rawat", "General Manoj Mukund Naravane", "General Dalbir Singh Suhag", "General Vijay Kumar Singh"],
                "correct_answer": "General Manoj Mukund Naravane"
            },
            {
                "question": "Which of the following is the oldest paramilitary force in India?",
                "options": ["Border Security Force (BSF)", "Central Reserve Police Force (CRPF)", "Assam Rifles", "Indo-Tibetan Border Police (ITBP)"],
                "correct_answer": "Assam Rifles"
            },
            {
                "question": "Who is the father of the Indian Navy?",
                "options": ["Admiral D.K. Joshi", "Admiral Sunil Lanba", "Admiral Karambir Singh", "Admiral Radhakrishna Hariram Tahiliani"],
                "correct_answer": "Admiral Radhakrishna Hariram Tahiliani"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.welcome_label = tk.Label(root, text="Welcome to the NDA Exam Quiz Game!", font=("Arial", 18, "bold"))
        self.welcome_label.pack(pady=20)
        
        self.rules_label = tk.Label(root, text="Rules:\n1. Answer the multiple-choice questions correctly.\n2. Each correct answer scores 1 point.", font=("Arial", 12))
        self.rules_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)
        
    def start_quiz(self):
        self.current_question = 0
        self.score = 0
        self.display_question()
        
    def display_question(self):
        if self.current_question < len(self.questions):
            self.clear_screen()
            question_data = self.questions[self.current_question]
            
            question_label = tk.Label(self.root, text=question_data["question"], font=("Arial", 14, "bold"))
            question_label.pack(pady=10)
            
            for option in question_data["options"]:
                option_button = tk.Button(self.root, text=option, command=lambda opt=option: self.check_answer(opt))
                option_button.pack(pady=5)
        else:
            self.show_results()
        
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect!", f"Sorry, your answer is incorrect.\nThe correct answer is: {correct_answer}")
        
        self.current_question += 1
        self.display_question()
        
    def show_results(self):
        self.clear_screen()
        result_label = tk.Label(self.root, text=f"Your Final Score: {self.score}/{len(self.questions)}", font=("Arial", 16, "bold"))
        result_label.pack(pady=20)
        
        play_again_button = tk.Button(self.root, text="Play Again", command=self.start_quiz)
        play_again_button.pack(pady=10)
        
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
