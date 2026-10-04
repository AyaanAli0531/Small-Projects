import tkinter as tk
from tkinter import messagebox
 
questions = [
    {
        "question": "What is the capital city of Japan?",
        "options": ["A. Paris", "B. Tokyo", "C. Beijing", "D. Moscow"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used in Python to define a function?",
        "options": ["A. func", "B. def", "C. fun", "D. function"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Earth", "C. Jupiter", "D. Venus"],
        "answer": "A"
    },
    {
        "question": "Who is known as the Father of Computer?",
        "options": [
            "A. Steve Jobs",
            "B. Bill Gates",
            "C. Alan Turing",
            "D. Charles Babbage"
        ],
        "answer": "D"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["A. Newton", "B. Einstein", "C. Thomas Edison", "D. Tesla"],
        "answer": "C"
    }
]
 
root = tk.Tk()
root.title("Quiz Game")
root.geometry("600x500")
root.resizable(False, False)
 
current_question = 0
score = 0
selected_answer = tk.StringVar()
 
title_label = tk.Label(
    root,
    text="WELCOME TO THE QUIZ GAME",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)
 
question_number = tk.Label(
    root,
    text="",
    font=("Arial", 13)
)
question_number.pack(pady=5)
 
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    wraplength=500
)
question_label.pack(pady=20)
 
option_buttons = []
 
for i in range(4):
    button = tk.Radiobutton(
        root,
        text="",
        variable=selected_answer,
        value="",
        font=("Arial", 13),
        anchor="w",
        width=35
    )
    button.pack(pady=5)
    option_buttons.append(button)
 
next_button = tk.Button(
    root,
    text="Next Question",
    font=("Arial", 13, "bold"),
    width=18
)
next_button.pack(pady=25)
 
 
def show_question():
    question = questions[current_question]
 
    question_number.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )
 
    question_label.config(
        text=question["question"]
    )
 
    for i in range(4):
        option_buttons[i].config(
            text=question["options"][i],
            value=question["options"][i][0]
        )
 
    selected_answer.set("")
 
 
def check_answer():
    global current_question
    global score
 
    user_answer = selected_answer.get()
 
    if user_answer == "":
        messagebox.showwarning(
            "No Answer",
            "Please select an option first!"
        )
        return
 
    correct_answer = questions[current_question]["answer"]
 
    if user_answer == correct_answer:
        score += 1
        messagebox.showinfo(
            "Correct!",
            "Your answer is correct!"
        )
    else:
        messagebox.showerror(
            "Wrong!",
            f"Your answer is wrong!\n"
            f"The correct option is {correct_answer}"
        )
 
    current_question += 1
 
    if current_question < len(questions):
        show_question()
    else:
        show_result()
 
 
def show_result():
    percentage = (score / len(questions)) * 100
 
    if score == 5:
        message = "Excellent! You got all answers correct!"
    elif score >= 3:
        message = "Well done! You are almost there!"
    else:
        message = "You need more practice! Better luck next time!"
 
    messagebox.showinfo(
        "Quiz Completed",
        f"Your Final Score: {score}/{len(questions)}\n"
        f"Percentage: {percentage:.0f}%\n\n"
        f"{message}"
    )
 
    root.destroy()
 
 
next_button.config(command=check_answer)
show_question()
root.mainloop()