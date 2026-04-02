import tkinter as tk
from tkinter import ttk, messagebox
import time
from game import RockPaperScissorsGame
from ai_player import AIPlayer

root = tk.Tk()
root.title("Rock-Paper-Scissors AI")
root.geometry("600x550")
root.resizable(False, False)

game = RockPaperScissorsGame()
ai = None  
player_name = ""
player_total_wins = 0
ai_total_wins = 0
selected_difficulty = tk.StringVar(value="easy")

#  HELPER FUNCTIONS 
def show_frame(frame):
    frame.tkraise()

def reset_game_state():
    game.player_score = 0
    game.ai_score = 0
    game.rounds_played = 0
    game.game_history = []

#  START SCREEN 
start_frame = tk.Frame(root, bg="#1f1f2e")
start_frame.place(relwidth=1, relheight=1)

start_label = tk.Label(start_frame, text="🎮 Rock-Paper-Scissors AI 🎮",
                       font=("Arial", 24, "bold"), fg="white", bg="#1f1f2e")
start_label.pack(pady=100)

def go_to_difficulty():
    show_frame(difficulty_frame)

start_button = tk.Button(start_frame, text="Start Game", font=("Arial", 16),
                         bg="#4ecca3", fg="white", width=20, command=go_to_difficulty)
start_button.pack(pady=20)

#  DIFFICULTY SELECTION SCREEN 
difficulty_frame = tk.Frame(root, bg="#252836")
difficulty_frame.place(relwidth=1, relheight=1)

diff_label = tk.Label(difficulty_frame, text="Select AI Difficulty", font=("Arial", 20, "bold"),
                      fg="white", bg="#252836")
diff_label.pack(pady=80)

def save_difficulty():
    global ai
    difficulty = selected_difficulty.get()
    ai = AIPlayer(difficulty=difficulty)
    show_frame(name_frame)

tk.Radiobutton(difficulty_frame, text="Easy AI (Random)", variable=selected_difficulty,
               value="easy", font=("Arial", 16), bg="#252836", fg="white", selectcolor="#4ecca3").pack(pady=10)
tk.Radiobutton(difficulty_frame, text="Smart AI (Hard)", variable=selected_difficulty,
               value="smart", font=("Arial", 16), bg="#252836", fg="white", selectcolor="#f05454").pack(pady=10)

diff_next_btn = tk.Button(difficulty_frame, text="Next", font=("Arial", 14),
                          bg="#ff8c42", fg="white", width=15, command=save_difficulty)
diff_next_btn.pack(pady=20)

# Back button to start
diff_back_btn = tk.Button(difficulty_frame, text="Back", font=("Arial", 12),
                          bg="#4ecca3", fg="white", width=10, command=lambda: show_frame(start_frame))
diff_back_btn.pack(pady=10)

#  PLAYER NAME SCREEN 
name_frame = tk.Frame(root, bg="#272640")
name_frame.place(relwidth=1, relheight=1)

name_label = tk.Label(name_frame, text="Enter your name:", font=("Arial", 18),
                      fg="white", bg="#272640")
name_label.pack(pady=50)

name_entry = tk.Entry(name_frame, font=("Arial", 16))
name_entry.pack(pady=10)

def save_name():
    global player_name
    player_name = name_entry.get().strip()
    if player_name == "":
        messagebox.showerror("Error", "Please enter your name!")
        return
    welcome_label.config(text=f"Welcome, {player_name}!")
    score_label.config(text=f"{player_name} Wins: 0 | AI Wins: 0")
    show_frame(game_frame)

next_button = tk.Button(name_frame, text="Next", font=("Arial", 14),
                        bg="#ff8c42", fg="white", width=15, command=save_name)
next_button.pack(pady=20)

# Back button to difficulty selection
name_back_btn = tk.Button(name_frame, text="Back", font=("Arial", 12),
                          bg="#4ecca3", fg="white", width=10,
                          command=lambda: show_frame(difficulty_frame))
name_back_btn.pack(pady=10)

#  GAMEPLAY SCREEN 
game_frame = tk.Frame(root, bg="#1f2430")
game_frame.place(relwidth=1, relheight=1)

welcome_label = tk.Label(game_frame, text="", font=("Arial", 20, "bold"),
                         fg="white", bg="#1f2430")
welcome_label.pack(pady=20)

score_label = tk.Label(game_frame, text="", font=("Arial", 16), fg="white", bg="#1f2430")
score_label.pack(pady=10)

choice_frame = tk.Frame(game_frame, bg="#1f2430")
choice_frame.pack(pady=30)

player_choice_var = tk.StringVar()
highlight_buttons = {}

def highlight(btn):
    for b in highlight_buttons.values():
        b.config(bg="#4ecca3")
    btn.config(bg="#f05454")

def select_choice(choice):
    player_choice_var.set(choice)
    highlight(highlight_buttons[choice])
    start_round_button.config(state="normal")

rock_btn = tk.Button(choice_frame, text="🪨 Rock", width=12, height=2,
                     bg="#4ecca3", fg="white", font=("Arial", 14),
                     command=lambda: select_choice("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(choice_frame, text="📄 Paper", width=12, height=2,
                     bg="#4ecca3", fg="white", font=("Arial", 14),
                     command=lambda: select_choice("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(choice_frame, text="✂️ Scissors", width=12, height=2,
                         bg="#4ecca3", fg="white", font=("Arial", 14),
                         command=lambda: select_choice("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

highlight_buttons = {"rock": rock_btn, "paper": paper_btn, "scissors": scissors_btn}

# Back button to name
game_back_btn = tk.Button(game_frame, text="Back", font=("Arial", 12),
                          bg="#4ecca3", fg="white", width=10,
                          command=lambda: show_frame(name_frame))
game_back_btn.pack(pady=10)

#  COUNTDOWN SCREEN 
countdown_frame = tk.Frame(root, bg="#0d1b2a")
countdown_frame.place(relwidth=1, relheight=1)

countdown_label = tk.Label(countdown_frame, text="", font=("Arial", 36),
                           fg="#f9f871", bg="#0d1b2a")
countdown_label.pack(pady=100)

progress = ttk.Progressbar(countdown_frame, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=20)

#  RESULT SCREEN 
result_frame = tk.Frame(root, bg="#1c1c1c")
result_frame.place(relwidth=1, relheight=1)

result_label_r = tk.Label(result_frame, text="", font=("Arial", 24, "bold"),
                          fg="white", bg="#1c1c1c")
result_label_r.pack(pady=20)

player_choice_label_r = tk.Label(result_frame, text="", font=("Arial", 16),
                                 fg="white", bg="#1c1c1c")
player_choice_label_r.pack(pady=5)

ai_choice_label_r = tk.Label(result_frame, text="", font=("Arial", 16),
                             fg="white", bg="#1c1c1c")
ai_choice_label_r.pack(pady=5)

total_wins_label = tk.Label(result_frame, text="", font=("Arial", 16),
                            fg="#f9f871", bg="#1c1c1c")
total_wins_label.pack(pady=10)

def play_again():
    show_frame(game_frame)

def exit_game():
    root.destroy()

continue_button = tk.Button(result_frame, text="Continue", font=("Arial", 14),
                            bg="#4ecca3", fg="white", width=15, command=play_again)
continue_button.pack(pady=10)

exit_button = tk.Button(result_frame, text="Exit", font=("Arial", 14),
                        bg="#f05454", fg="white", width=15, command=exit_game)
exit_button.pack()

#  GAME LOGIC 
def start_round():
    global player_total_wins, ai_total_wins

    choice = player_choice_var.get()
    if choice == "":
        messagebox.showerror("Error", "Please select a choice!")
        return

    show_frame(countdown_frame)
    countdown_label.config(text="")
    progress['value'] = 0
    root.update()

    ai_choice = ai.make_choice()

    # Countdown with progress bar
    for i in range(3, 0, -1):
        countdown_label.config(text=str(i))
        progress['value'] = (3 - i + 1) * 33
        root.update()
        time.sleep(1)

    countdown_label.config(text="Shoot! 🎯")
    progress['value'] = 100
    root.update()
    time.sleep(1)

    # Determine winner
    result = game.determine_winner(choice, ai_choice)
    game.update_scores(result)
    ai.learn_from_move(choice)

    # Update total wins
    if result == "player":
        player_total_wins += 1
    elif result == "ai":
        ai_total_wins += 1

    # Show result screen
    player_choice_label_r.config(text=f"{player_name} chose: {choice}")
    ai_choice_label_r.config(text=f"AI chose: {ai_choice}")
    total_wins_label.config(text=f"{player_name} Total Wins: {player_total_wins} | AI Total Wins: {ai_total_wins}")

    if result == "player":
        result_label_r.config(text="🎉 You Win!")
    elif result == "ai":
        result_label_r.config(text="🤖 AI Wins!")
    else:
        result_label_r.config(text="🤝 It's a Tie!")

    show_frame(result_frame)

start_round_button = tk.Button(game_frame, text="Start Round", font=("Arial", 14),
                               bg="#f9f871", fg="black", width=15, state="disabled",
                               command=start_round)
start_round_button.pack(pady=20)

#  INITIALIZE 
show_frame(start_frame)
root.mainloop()
