import customtkinter as ctk
import tkinter as tk
from pyker.models import classify_hand

class PokerHelperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Helper")
        self.root.configure(bg='#2c3e50')  # Set background of the main window to dark
        self.players = []

        self.ask_num_players()

    def ask_num_players(self):
        num_players = tk.simpledialog.askinteger("Number of Players", "Enter number of players:", minvalue=2, maxvalue=10)
        if num_players:
            self.num_players = num_players
            self.create_widgets()

    def create_widgets(self):
        round_frame = ctk.CTkFrame(self.root, fg_color='#2c3e50', corner_radius=10)
        round_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(round_frame, text="Round Number:", fg_color='#2c3e50', text_color='#ecf0f1').grid(row=0, column=0, padx=5, pady=5)
        self.round_entry = ctk.CTkEntry(round_frame, fg_color='#34495e', text_color='#ecf0f1')
        self.round_entry.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(round_frame, text="Community Cards:", fg_color='#2c3e50', text_color='#ecf0f1').grid(row=1, column=0, padx=5, pady=5)
        self.community_cards_entry = ctk.CTkEntry(round_frame, fg_color='#34495e', text_color='#ecf0f1')
        self.community_cards_entry.grid(row=1, column=1, padx=5, pady=5)

        self_info_frame = ctk.CTkFrame(self.root, fg_color='#2c3e50', corner_radius=10)
        self_info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(self_info_frame, text="Your Hand:", fg_color='#2c3e50', text_color='#ecf0f1').grid(row=0, column=0, padx=5, pady=5)
        self.hand_entry = ctk.CTkEntry(self_info_frame, fg_color='#34495e', text_color='#ecf0f1')
        self.hand_entry.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self_info_frame, text="Your Bet:", fg_color='#2c3e50', text_color='#ecf0f1').grid(row=1, column=0, padx=5, pady=5)
        self.bet_entry = ctk.CTkEntry(self_info_frame, fg_color='#34495e', text_color='#ecf0f1')
        self.bet_entry.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkButton(self_info_frame, text="Record Bet", command=self.record_own_bet, corner_radius=10).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        ctk.CTkButton(self_info_frame, text="Evaluate Hand", command=self.evaluate_hand, corner_radius=10).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.hand_eval_label = ctk.CTkLabel(self_info_frame, text="", fg_color='#2c3e50', text_color='#ecf0f1')
        self.hand_eval_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.table_frame = ctk.CTkFrame(self.root, fg_color='#2c3e50', corner_radius=10)
        self.table_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        for i in range(self.num_players):
            p_frame = ctk.CTkFrame(self.table_frame, fg_color='#2c3e50', corner_radius=10)
            p_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="ew")

            ctk.CTkLabel(p_frame, text=f"Player {i+1}", fg_color='#2c3e50', text_color='#ecf0f1').grid(row=0, column=0, padx=5, pady=5)
            name_entry = ctk.CTkEntry(p_frame, fg_color='#34495e', text_color='#ecf0f1')
            name_entry.grid(row=0, column=1, padx=5, pady=5)

            ctk.CTkLabel(p_frame, text="Bet:", fg_color='#2c3e50', text_color='#ecf0f1').grid(row=1, column=0, padx=5, pady=5)
            bet_entry = ctk.CTkEntry(p_frame, fg_color='#34495e', text_color='#ecf0f1')
            bet_entry.grid(row=1, column=1, padx=5, pady=5)

            ctk.CTkButton(p_frame, text="Bet", command=lambda i=i: self.record_bet(i), corner_radius=10).grid(row=2, column=0, padx=5, pady=5)
            ctk.CTkButton(p_frame, text="Fold", command=lambda i=i: self.record_fold(i), corner_radius=10).grid(row=2, column=1, padx=5, pady=5)

            player_info = {
                'name': name_entry,
                'bet': bet_entry,
            }
            self.players.append(player_info)

        self.results = ctk.CTkTextbox(self.root, height=10, width=50, fg_color='#34495e', text_color='#ecf0f1')
        self.results.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def record_own_bet(self):
        round_num = self.round_entry.get()
        bet_amount = self.bet_entry.get()
        hand = self.hand_entry.get()
        community_cards = self.community_cards_entry.get()
        self.results.insert("end", f"Your hand: {hand}, Your bet: {bet_amount} in round {round_num}, Community cards: {community_cards}.\n")

    def evaluate_hand(self):
        hand = self.hand_entry.get().split()
        community_cards = self.community_cards_entry.get().split()

        try:
            score, hand_type, best_hand = classify_hand(hand, community_cards)
            self.hand_eval_label.config(text=f"Best hand: {best_hand}, Hand type: {hand_type}, Score: {score}")
        except ValueError as e:
            self.hand_eval_label.config(text=str(e))

    def record_bet(self, idx):
        p_info = self.players[idx]
        player = p_info['name'].get()
        round_num = self.round_entry.get()
        bet_amount = p_info['bet'].get()
        self.results.insert("end", f"Player {player} bets {bet_amount} in round {round_num}.\n")

    def record_fold(self, idx):
        p_info = self.players[idx]
        player = p_info['name'].get()
        round_num = self.round_entry.get()
        self.results.insert("end", f"Player {player} folds in round {round_num}.\n")

if __name__ == "__main__":
    root = ctk.CTk()
    app = PokerHelperGUI(root)
    root.mainloop()
