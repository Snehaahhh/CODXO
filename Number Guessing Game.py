import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    attempts_left.set(10)
    feedback_label.config(text="")
    entry_guess.delete(0, tk.END)

# Function to check the guess
def check_guess():
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return
    
    attempts = attempts_left.get()
    attempts -= 1
    attempts_left.set(attempts)
    
    if guess == secret_number:
        messagebox.showinfo("Congratulations!", f"You guessed the number {secret_number}!")
        new_game()
    elif guess < secret_number:
        feedback_label.config(text="Too low!")
    else:
        feedback_label.config(text="Too high!")
    
    if attempts == 0:
        messagebox.showinfo("Game Over", f"The secret number was {secret_number}. Game Over!")
        new_game()

# Main window setup
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("300x200")

# Frame for game controls
frame = tk.Frame(window)
frame.pack(pady=10)

# Attempts left
attempts_left = tk.IntVar()
attempts_left.set(10)
attempts_label = tk.Label(frame, textvariable=attempts_left)
attempts_label.grid(row=0, column=0, padx=10)

# Guess entry
entry_guess = tk.Entry(frame, width=10)
entry_guess.grid(row=0, column=1, padx=10)

# Guess button
guess_button = tk.Button(frame, text="Guess", command=check_guess)
guess_button.grid(row=0, column=2, padx=10)

# Feedback label
feedback_label = tk.Label(window, text="", fg="blue")
feedback_label.pack(pady=10)

# New game button
new_game_button = tk.Button(window, text="New Game", command=new_game)
new_game_button.pack()

# Start the game
new_game()

window.mainloop()
