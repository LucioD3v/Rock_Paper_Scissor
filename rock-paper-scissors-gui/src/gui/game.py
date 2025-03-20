from tkinter import Tk, Label, Button, StringVar, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.comp_score = 0

        self.score_label = Label(master, text="Scores: You 0 - 0 Computer")
        self.score_label.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

        self.rock_button = Button(master, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack()

        self.paper_button = Button(master, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack()

        self.scissors_button = Button(master, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack()

        self.play_again_button = Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack()

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        if user_choice == comp_choice:
            self.result_label.config(text=f"It's a draw! Computer chose {comp_choice}.")
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            self.user_score += 1
            self.result_label.config(text=f"You win! Computer chose {comp_choice}.")
        else:
            self.comp_score += 1
            self.result_label.config(text=f"You lose! Computer chose {comp_choice}.")

        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Scores: You {self.user_score} - {self.comp_score} Computer")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.result_label.config(text="")
        self.update_score()

def main():
    root = Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()