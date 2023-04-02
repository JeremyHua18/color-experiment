import tkinter as tk
import random
import time

colors = {
    "red": "red",
    "blue": "blue",
    "green": "green",
    "yellow": "yellow",
    "purple": "purple",
}

class ColorsPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("Monolingual Colors Puzzle")

        self.color_label = tk.Label(self.master, font=("Arial", 30))
        self.color_label.pack(pady=20)

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)

        for color in colors:
            canvas = tk.Canvas(self.buttons_frame, width=100, height=50, bd=0, highlightthickness=0)
            canvas.pack(side="left", padx=10)
            canvas.create_rectangle(0, 0, 100, 50, fill=color, outline=color)
            canvas.bind("<Button-1>", lambda event, c=color: self.check_answer(c))

        self.result_label = tk.Label(self.master, font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(self.master, text="Restart", font=("Arial", 14), command=self.reset)
        self.reset_button.pack(pady=10)

        self.reset()

    def reset(self):
        self.start_time = time.time()
        self.correct = 0
        self.total = 0
        self.new_question()

    def new_question(self):
        self.color_key = random.choice(list(colors.keys()))
        self.color_name = colors[self.color_key]
        self.color_label.config(text=self.color_name)
        self.result_label.config(text="")

    def check_answer(self, selected_color):
        self.total += 1
        if selected_color == self.color_key:
            self.correct += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text="Incorrect!", fg="red")

        elapsed_time = time.time() - self.start_time
        accuracy = (self.correct / self.total) * 100
        self.master.title(f"Accuracy: {accuracy:.2f}% - Time: {elapsed_time:.2f} s")

        self.new_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorsPuzzle(root)
    root.mainloop()
