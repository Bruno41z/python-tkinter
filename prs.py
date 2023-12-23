import tkinter as tk
import random
from tkinter import messagebox

class Application:

    def __init__(self, window):
        self.window = window
        self.window.configure(bg="black")

        self.main_menu = tk.Menu(self.window)
        self.window.config(menu=self.main_menu)

        self.game_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Game", menu=self.game_menu)
        self.game_menu.add_command(label="New Game", command=self.new_game)
        self.game_menu.add_separator()
        self.game_menu.add_command(label="Close", command=self.close_application)

        self.button_paper = tk.Button(self.window, text="Paper", fg="white", bg="orange", command=lambda: self.player_choice(1))
        self.button_paper.pack(side=tk.TOP)

        self.button_rock = tk.Button(self.window, text="Rock", fg="white", bg="orange", command=lambda: self.player_choice(2))
        self.button_rock.pack(side=tk.TOP)

        self.button_scissors = tk.Button(self.window, text="Scissors", fg="white", bg="orange", command=lambda: self.player_choice(3))
        self.button_scissors.pack(side=tk.TOP)

        self.result_label = tk.Label(self.window, text="", fg="white", bg="black")
        self.result_label.pack()

        self.close_button = tk.Button(self.window, text="Close Application", command=self.close_application)
        self.close_button.pack(side="bottom")

        self.player_score = 0
        self.computer_score = 0
        self.rounds = 0

    def player_choice(self, choice):
        self.player_selection = choice
        self.computer_selection = random.randint(1, 3)

        if self.player_selection == self.computer_selection:
            result = "It's a tie!"
        elif (self.player_selection == 1 and self.computer_selection == 2) or (self.player_selection == 2 and self.computer_selection == 3) or (self.player_selection == 3 and self.computer_selection == 1):
            self.player_score += 1
            result = "You win!"
        else:
            self.computer_score += 1
            result = "You lose!"

        self.rounds += 1
        self.result_label.config(text=f"Round {self.rounds}: {result} - Your Score: {self.player_score} | Computer Score: {self.computer_score}")

    def close_application(self):
        response = messagebox.askyesno("Closing Application", "Are you sure you want to close the application?")
        if response:
            self.window.destroy()

    def new_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.result_label.config(text="")
        messagebox.showinfo("New Game", "New game started!")

window = tk.Tk()
app = Application(window)
window.resizable(False, False)
window.geometry("500x300")
window.title("Rock Paper Scissors")
window.mainloop()
