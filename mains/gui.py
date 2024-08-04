import tkinter as tk
from tkinter import ttk, simpledialog

class PokerHelperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Helper")
        self.root.configure(bg='#2c3e50')
        self.players = []

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#2c3e50')
        self.style.configure('TLabel', background='#2c3e50', foreground='#ecf0f1', font=('Helvetica', 12))
        self.style.configure('TButton', background='#2c3e50', foreground='#ecf0f1', font=('Helvetica', 12, 'bold'), padding=10)
        self.style.map('TButton', background=[('active', '#34495e')], foreground=[('active', '#ecf0f1')])
        self.style.configure('TEntry', fieldbackground='#34495e', foreground='#ecf0f1', font=('Helvetica', 12))
        self.style.configure('TLabelframe', background='#2c3e50', foreground='#ecf0f1', font=('Helvetica', 12, 'bold'), padding=10)
        self.style.configure('TLabelframe.Label', background='#2c3e50', foreground='#ecf0f1', font=('Helvetica', 12, 'bold'), padding=5)

        self.ask_num_players()

    def ask_num_players(self):
        num_players = simpledialog.askinteger("Number of Players", "Enter number of players:", minvalue=2, maxvalue=10)
        if num_players:
            self.num_players = num_players
            self.create_widgets()

    def create_widgets(self):
        # Frame for round number and community cards
        round_frame = ttk.Frame(self.root, padding="10")
        round_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(round_frame, text="Round Number:").grid(row=0, column=0, padx=5, pady=5)
        self.round_entry = ttk.Entry(round_frame)
        self.round_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(round_frame, text="Community Cards:").grid(row=1, column=0, padx=5, pady=5)
        self.community_cards_entry = ttk.Entry(round_frame)
        self.community_cards_entry.grid(row=1, column=1, padx=5, pady=5)

        # Frame for player's own information
        self_info_frame = ttk.LabelFrame(self.root, text="Your Info", padding="10")
        self_info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self_info_frame, text="Your Hand:").grid(row=0, column=0, padx=5, pady=5)
        self.hand_entry = ttk.Entry(self_info_frame)
        self.hand_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self_info_frame, text="Your Bet:").grid(row=1, column=0, padx=5, pady=5)
        self.bet_entry = ttk.Entry(self_info_frame)
        self.bet_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self_info_frame, text="Record Bet", command=self.record_own_bet).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Frame for other players
        self.table_frame = ttk.Frame(self.root, padding="10")
        self.table_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        for i in range(self.num_players):
            p_frame = ttk.LabelFrame(self.table_frame, text=f"Player {i+1}")
            p_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="ew")

            ttk.Label(p_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
            name_entry = ttk.Entry(p_frame)
            name_entry.grid(row=0, column=1, padx=5, pady=5)

            ttk.Label(p_frame, text="Bet:").grid(row=1, column=0, padx=5, pady=5)
            bet_entry = ttk.Entry(p_frame)
            bet_entry.grid(row=1, column=1, padx=5, pady=5)

            ttk.Button(p_frame, text="Bet", command=lambda i=i: self.record_bet(i)).grid(row=2, column=0, padx=5, pady=5)
            ttk.Button(p_frame, text="Fold", command=lambda i=i: self.record_fold(i)).grid(row=2, column=1, padx=5, pady=5)

            player_info = {
                'name': name_entry,
                'bet': bet_entry,
            }
            self.players.append(player_info)

        self.results = tk.Text(self.root, height=10, width=50, background='#34495e', foreground='#ecf0f1', font=('Helvetica', 12))
        self.results.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def record_own_bet(self):
        round_num = self.round_entry.get()
        bet_amount = self.bet_entry.get()
        hand = self.hand_entry.get()
        community_cards = self.community_cards_entry.get()
        self.results.insert(tk.END, f"Your hand: {hand}, Your bet: {bet_amount} in round {round_num}, Community cards: {community_cards}.\n")

    def record_bet(self, idx):
        p_info = self.players[idx]
        player = p_info['name'].get()
        round_num = self.round_entry.get()
        bet_amount = p_info['bet'].get()
        self.results.insert(tk.END, f"Player {player} bets {bet_amount} in round {round_num}.\n")

    def record_fold(self, idx):
        p_info = self.players[idx]
        player = p_info['name'].get()
        round_num = self.round_entry.get()
        self.results.insert(tk.END, f"Player {player} folds in round {round_num}.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerHelperGUI(root)
    root.mainloop()
