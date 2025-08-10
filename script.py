import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe with Scoreboard")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
score = {"X": 0, "O": 0}

# Colors for players
colors = {"X": "blue", "O": "red"}

def check_winner():
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        # Check cols
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

def update_scoreboard():
    score_label.config(text=f"Score - X: {score['X']}   O: {score['O']}")

def update_turn_label():
    turn_label.config(text=f"Turn: Player {current_player}", fg=colors[current_player])

def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, fg=colors[current_player], state="disabled")
        
        winner = check_winner()
        if winner:
            score[winner] += 1
            update_scoreboard()
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            update_turn_label()

def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")
    update_turn_label()

# UI setup

# Scoreboard label
score_label = tk.Label(root, text="Score - X: 0   O: 0", font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=3, pady=(10,0))

# Turn label
turn_label = tk.Label(root, text="Turn: Player X", font=("Arial", 14), fg=colors["X"])
turn_label.grid(row=1, column=0, columnspan=3, pady=(0,10))

# Create buttons grid
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 32, "bold"), width=5, height=2,
                        command=lambda r=i, c=j: button_click(r, c))
        btn.grid(row=i+2, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# Reset button
reset_btn = tk.Button(root, text="Reset Score & Board", font=("Arial", 12), command=lambda: [reset_board(), reset_score()])
reset_btn.grid(row=5, column=0, columnspan=3, pady=10)

def reset_score():
    score["X"] = 0
    score["O"] = 0
    update_scoreboard()

root.mainloop()
