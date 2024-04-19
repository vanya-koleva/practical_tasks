import tkinter as tk
from tkinter import messagebox
import random


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        # Define the categories and their corresponding words
        self.categories = {
            "Animals": ["cat", "dog", "elephant", "giraffe", "monkey"],
            "Countries": ["india", "japan", "brazil", "australia", "canada"],
            "Fruits": ["apple", "banana", "orange", "grape", "kiwi"]
        }
        self.current_category = ""
        self.secret_word = ""
        self.guesses_left = 6
        self.guesses = set()  # The set of letters the player has guessed
        self.score = 0

        # Create the canvas for drawing the hangman
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        # Create the label for displaying the category
        self.category_label = tk.Label(master, text="Category: ")
        self.category_label.pack()

        # Create the label for displaying the secret word
        self.word_display = tk.Label(master, text="", font=("Helvetica", 20))
        self.word_display.pack()

        # Create the label for the guess prompt
        self.label = tk.Label(master, text="Guess a letter:")
        self.label.pack()

        # Create the input field for the player's guess
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Create the guess button and bind it to the guess_letter method
        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack()

        # Create the new word button and bind it to the choose_new_word method
        self.new_word_button = tk.Button(master, text="New Word", command=self.choose_new_word)
        self.new_word_button.pack()

        # Create the label for displaying the score
        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()

        # Create the listbox for displaying the categories
        self.category_listbox = tk.Listbox(self.master, height=len(self.categories))
        for category in self.categories.keys():
            self.category_listbox.insert(tk.END, category)
        self.category_listbox.pack()

        # Create the choose category button and bind it to the choose_category method
        choose_button = tk.Button(self.master, text="Choose Category", command=self.choose_category)
        choose_button.pack()

    def choose_category(self):
        """Allow the player to choose a category and set the current_category attribute"""
        if self.category_listbox.curselection():
            index = self.category_listbox.curselection()[0]
            self.current_category = self.category_listbox.get(index)
            self.category_label['text'] = "Category: " + self.current_category
            self.choose_new_word()

    def choose_new_word(self):
        """Choose a random new word from the selected category and reset the game attributes"""
        self.secret_word = random.choice(self.categories[self.current_category])
        self.guesses_left = 6
        self.guesses = set()
        self.update_word_display()
        self.draw_hangman()

    def draw_hangman(self):
        """Draw the hang and the hangman based on the number of incorrect guesses"""
        self.canvas.delete("all")
        # Draw the hang
        self.canvas.create_line(50, 350, 150, 350)
        self.canvas.create_line(100, 350, 100, 50)
        self.canvas.create_line(100, 50, 200, 50)
        self.canvas.create_line(200, 50, 200, 100)
        # Draw the hangman
        if self.guesses_left < 6:
            self.canvas.create_oval(180, 100, 220, 140)  # head
        if self.guesses_left < 5:
            self.canvas.create_line(200, 140, 200, 200)  # body
        if self.guesses_left < 4:
            self.canvas.create_line(200, 160, 180, 140)  # left arm
        if self.guesses_left < 3:
            self.canvas.create_line(200, 160, 220, 140)  # right arm
        if self.guesses_left < 2:
            self.canvas.create_line(200, 200, 180, 240)  # left leg
        if self.guesses_left < 1:
            self.canvas.create_line(200, 200, 220, 240)  # right leg

    def guess_letter(self):
        """Process player's guess and update the game state accordingly"""
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        # Check if the guess is valid
        if not self.current_category:
            messagebox.showerror("No Category Selected", "Please select a category before guessing.")
        elif len(guess) != 1:
            messagebox.showerror("Invalid input", "Please enter a single letter.")
        elif guess in self.guesses:
            messagebox.showinfo("Already guessed", "You have already guessed that letter.")
        else:
            # If the guess is valid and hasn't been guessed before, add it to the set of guesses
            self.guesses.add(guess)
            # Check if the guessed letter is in the secret word
            if guess in self.secret_word:
                self.score += 1
                self.update_word_display()
                # Check if all the letters in the secret word have been guessed
                if set(self.secret_word) <= self.guesses:
                    messagebox.showinfo("Congratulations", "You guessed the word!")
                    self.score += 5
                    self.choose_new_word()
            else:
                # If the guessed letter is not in the secret word
                self.guesses_left -= 1
                self.score -= 1
                self.draw_hangman()
                # Check if there are no guesses left
                if self.guesses_left == 0:
                    messagebox.showinfo("Game over", "The word was " + self.secret_word)
                    self.choose_new_word()
        # Update the score label with the current score
        self.score_label['text'] = "Score: " + str(self.score)

    def update_word_display(self):
        """Update the displayed word with the guessed letters"""
        displayed_word = [letter if letter in self.guesses else '_' for letter in self.secret_word]
        self.word_display['text'] = ' '.join(displayed_word)


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
