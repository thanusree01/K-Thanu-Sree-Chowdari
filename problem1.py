import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10)
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 14), width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
    def on_button_click(self, char):
        if char == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)  # Safe here since only calculator input
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except ZeroDivisionError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid")
        else:
            self.entry.insert(tk.END, char)
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
