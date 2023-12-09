import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Memória")

        self.sequence = []
        self.user_input = []
        self.score = 0

        self.create_widgets()
        self.play_game()

    def create_widgets(self):
        self.led_frame = tk.Frame(self.master)
        self.led_frame.pack(pady=20)

        self.led_labels = []
        for i in range(3):
            label = tk.Label(self.led_frame, text=f"LED {i+1}", font=("Arial", 24), width=10, height=2, relief="solid")
            label.pack(side="left", padx=10)
            self.led_labels.append(label)

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=20)

        self.button1 = tk.Button(self.button_frame, text="BOTÃO 1", command=lambda: self.get_user_input(0), font=("Arial", 12), width=10)
        self.button1.pack(side="left", padx=10)

        self.button2 = tk.Button(self.button_frame, text="BOTÃO 2", command=lambda: self.get_user_input(1), font=("Arial", 12), width=10)
        self.button2.pack(side="left", padx=10)

        self.button3 = tk.Button(self.button_frame, text="BOTÃO 3", command=lambda: self.get_user_input(2), font=("Arial", 12), width=10)
        self.button3.pack(side="left", padx=10)

        self.control_frame = tk.Frame(self.master)
        self.control_frame.pack(pady=20)

        self.start_button = tk.Button(self.control_frame, text="INICIAR", command=self.play_game, font=("Arial", 12), bg="green", width=10)
        self.start_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.control_frame, text="REINICIAR", command=self.reset_game, font=("Arial", 12), bg="yellow", width=10)
        self.reset_button.pack(side="left", padx=10)

        self.exit_button = tk.Button(self.control_frame, text="SAIR", command=self.master.quit, font=("Arial", 12), bg="red", width=10)
        self.exit_button.pack(side="left", padx=10)

    def display_sequence(self):
        for i in self.sequence:
            self.led_labels[i]['bg'] = 'green'
            self.master.update()
            time.sleep(1)
            self.led_labels[i]['bg'] = 'white'
            self.master.update()
            time.sleep(0.5)

    def get_user_input(self, index):
        self.user_input.append(index)
        self.led_labels[index]['bg'] = 'blue'
        self.master.update()
        time.sleep(0.2)
        self.led_labels[index]['bg'] = 'white'
        self.master.update()

        if self.user_input[-1] != self.sequence[len(self.user_input) - 1]:
            messagebox.showinfo("Result", "Wrong! Game over.")
            self.reset_game()
        elif len(self.user_input) == len(self.sequence):
            messagebox.showinfo("Result", "Correct! Next level.")
            self.user_input = []
            self.score += 1 
            self.score_label['text'] = f"Score: {self.score}"
            self.play_game() 

    def play_game(self):
        self.sequence.append(random.choice([0, 1, 2]))
        self.display_sequence()

    def reset_game(self):
        self.user_input = []  
        self.sequence = [] 
        self.score = 0 
        self.score_label['text'] = f"Score: {self.score}"

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2) - (600 / 2)

    root.geometry("+%d+%d" % (x, y))

    game = MemoryGame(root)
    root.mainloop()