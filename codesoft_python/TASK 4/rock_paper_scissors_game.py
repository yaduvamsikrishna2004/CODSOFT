import tkinter as tk
from tkinter import messagebox
import random

# Game Logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_round(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    result_label.config(text=f"User chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"User Score: {user_score}   Computer Score: {computer_score}")
    play_again_button.pack(pady=10)  # Show the play again button after a round

def play_again():
    result_label.config(text="")
    play_again_button.pack_forget()  # Hide the play again button

# Set up the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg="#ADD8E6")  # Light blue background

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

# Create UI elements
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16), bg="#ADD8E6")
title_label.pack(pady=10)

buttons_frame = tk.Frame(root, bg="#ADD8E6")
buttons_frame.pack(pady=10)

rock_button = tk.Button(buttons_frame, text="Rock", width=10, command=lambda: play_round("Rock"), bg="#A9A9A9")  # Dark gray button
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(buttons_frame, text="Paper", width=10, command=lambda: play_round("Paper"), bg="#FFFFE0")  # Light yellow button
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(buttons_frame, text="Scissors", width=10, command=lambda: play_round("Scissors"), bg="#F08080")  # Light coral button
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#ADD8E6")
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"User Score: {user_score}   Computer Score: {computer_score}", font=("Helvetica", 12), bg="#ADD8E6")
score_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", command=play_again, bg="#FFD700")  # Gold button
play_again_button.pack(pady=10)
play_again_button.pack_forget()  # Hide the play again button initially

# Start the main event loop
root.mainloop()
