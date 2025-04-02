import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        
        # Create a 3x3 grid of buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)
        
        self.window.mainloop()
    
    def make_move(self, row, col):
        # If the button is already clicked, do nothing
        if self.buttons[row][col]["text"] != "":
            return
        
        # Update the button text with the current player's symbol
        self.buttons[row][col]["text"] = self.current_player
        
        # Check for a winner or a draw
        if self.check_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_board()
        elif self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()
        else:
            # Switch to the other player
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != "":
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False
    
    def check_draw(self):
        # Check if all buttons are filled and no winner
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    return False
        return True
    
    def reset_board(self):
        # Clear the board for a new game
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = "X"

# Run the game
if __name__ == "__main__":
    TicTacToe()
