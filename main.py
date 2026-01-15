from XNOR_module import CLIPBOARD_AVAILABLE, copy_to_clipboard, cls
import tkinter as tk
from tkinter import messagebox

#game
gamewin_1 = []
game = 1

def say_hi(letter):
    global game

    if game == 1:
        if letter == "D":
            messagebox.showinfo("Round 1", "YOU WIN ROUND 1")
            game = 2
            show_question()  # show round 2
        else:
            messagebox.showinfo("Round 1", "YOU DONT WIN ROUND 1")
            root.destroy()
    elif game == 2:
        if letter == "A":
            messagebox.showinfo("Round 2", "YOU WIN ROUND 2")
        else:
            messagebox.showinfo("Round 2", "YOU DONT WIN ROUND 2")
        root.destroy()

def show_question():
    # clear previous labels in top_frame
    for widget in top_frame.winfo_children():
        widget.destroy()

    if game == 1:
        question_label = tk.Label(top_frame, text="Did 9/11 happen in....", font=("Arial", 14))
        question_label.pack(pady=10)
        answers_label = tk.Label(top_frame, text="A 2022   B 2005\nC 2015   D 2001", font=("Arial", 12))
        answers_label.pack(pady=10)
    elif game == 2:
        question_label = tk.Label(top_frame, text="Which country starts with B and is the biggest?", font=("Arial", 14), wraplength=280, justify="left")
        question_label.pack(pady=10)
        answers_label = tk.Label(top_frame, text="A Brazil   B Bulgaria\nC Burkina Faso   D Brunei", font=("Arial", 12))
        answers_label.pack(pady=10)

# Tkinter window
root = tk.Tk()
root.title("Buttons for Game")
root.geometry("301x551")

# Frames
top_frame = tk.Frame(root)
top_frame.pack(fill="both", expand=True, pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# show first question
show_question()

# Buttons
for letter in ["A", "B", "C", "D"]:
    tk.Button(
        bottom_frame,
        text=letter,
        font=("Arial", 18, "bold"),
        width=8,
        height=2,
        command=lambda l=letter: say_hi(l)
    ).pack(pady=6)

root.mainloop()