import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Helper")

        self.create_widgets()

    def create_widgets(self):
        # player info
        player_frame = ttk.LabelFrame(self.root, text="Player Information")
        player_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # name box
        player_name_label = ttk.Label(player_frame, text="Player Name:")
        player_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.player_name_entry = ttk.Entry(player_frame)
        self.player_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # round number box
        round_label = ttk.Label(player_frame, text="Round Number:")
        round_label.grid(row=1, column=0, padx=5, pady=5)
        self.round_entry = ttk.Entry(player_frame)
        self.round_entry.grid(row=1, column=1, padx=5, pady=5)

        # bet box
        bet_amount_label = ttk.Label(player_frame, text="Bet Amount:")
        bet_amount_label.grid(row=2, column=0, padx=5, pady=5)
        self.bet_amount_entry = ttk.Entry(player_frame)
        self.bet_amount_entry.grid(row=2, column=1, padx=5, pady=5)

        # hand box
        hand_label = ttk.Label(player_frame, text="Hand:")
        hand_label.grid(row=3, column=0, padx=5, pady=5)
        self.hand_entry = ttk.Entry(player_frame)
        self.hand_entry.grid(row=3, column=1, padx=5, pady=5)

        # action buttons
        bet_button = ttk.Button(player_frame, text="Bet", command=self.record_bet)
        bet_button.grid(row=4, column=0, padx=5, pady=5)
        fold_button = ttk.Button(player_frame, text="Fold", command=self.record_fold)
        fold_button.grid(row=4, column=1, padx=5, pady=5)
        show_hand_button = ttk.Button(player_frame, text="Show Hand", command=self.show_hand)
        show_hand_button.grid(row=4, column=2, padx=5, pady=5)

        # result display
        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def record_bet(self):
        player = self.player_name_entry.get()
        round_num = self.round_entry.get()
        bet_amount = self.bet_amount_entry.get()
        self.results_text.insert(tk.END, f"Player {player} bets {bet_amount} in round {round_num}.\n")

    def record_fold(self):
        player = self.player_name_entry.get()
        round_num = self.round_entry.get()
        self.results_text.insert(tk.END, f"Player {player} folds in round {round_num}.\n")

    def show_hand(self):
        player = self.player_name_entry.get()
        round_num = self.round_entry.get()
        hand = self.hand_entry.get()
        self.results_text.insert(tk.END, f"Player {player} shows hand {hand} in round {round_num}.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
