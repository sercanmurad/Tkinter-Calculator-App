import tkinter as tk
from tkinter import ttk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying numbers and results
        self.entry = ttk.Entry(self.root, font=("Arial", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Button layout and properties
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons dynamically
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        # Style buttons with ttk for modern look
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 18), padding=10)

        btn = ttk.Button(self.root, text=text, command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, sticky="news", padx=5, pady=5)

        # Make the window responsive
        self.root.grid_rowconfigure(row, weight=1)
        self.root.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        # Handle button presses
        if char == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)  # Evaluate the expression
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == "C":
            self.entry.delete(0, tk.END)  # Clear the entry field
        else:
            # Append character to the entry field
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current + char)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
