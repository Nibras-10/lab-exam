"""
A simple Tkinter program that shows the basics:
- Creating a window and widgets (Label, Entry, Button, Listbox)
- Handling button clicks and the Enter key
- Updating a status bar
"""

import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root: tk.Tk) -> None:
        root.title("Simple Tkinter Demo")
        root.geometry("400x300")  # width x height

        # Main content frame with a bit of padding
        frame = tk.Frame(root, padx=12, pady=12)
        frame.pack(fill="both", expand=True)

        # Label + Entry
        tk.Label(frame, text="Enter your name:").grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar()
        entry = tk.Entry(frame, textvariable=self.name_var, width=28)
        entry.grid(row=0, column=1, padx=6, sticky="ew")
        entry.bind("<Return>", self.greet)  # Press Enter to trigger greet

        # Greet button
        tk.Button(frame, text="Greet", command=self.greet).grid(row=0, column=2, padx=4)

        # Listbox area
        tk.Label(frame, text="Messages:").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.listbox = tk.Listbox(frame, height=8)
        self.listbox.grid(row=2, column=0, columnspan=3, sticky="nsew")

        # Make the listbox row/entry column grow with the window
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        # Action buttons
        btns = tk.Frame(frame)
        btns.grid(row=3, column=0, columnspan=3, sticky="e", pady=8)
        tk.Button(btns, text="Add to list", command=self.add_to_list).pack(side="left", padx=4)
        tk.Button(btns, text="Clear list", command=self.clear_list).pack(side="left", padx=4)
        tk.Button(btns, text="Quit", command=root.destroy).pack(side="left", padx=4)

        # Simple status bar at the bottom
        self.status_var = tk.StringVar(value="Ready")
        status = tk.Label(root, textvariable=self.status_var, anchor="w", relief="sunken")
        status.pack(fill="x", side="bottom")

    def greet(self, event=None) -> None:
        name = self.name_var.get().strip() or "there"
        msg = f"Hello, {name}!"
        messagebox.showinfo("Greeting", msg)
        self.status_var.set("Greeted user")

    def add_to_list(self) -> None:
        text = self.name_var.get().strip()
        if not text:
            self.status_var.set("Type something first")
            return
        self.listbox.insert("end", text)
        self.status_var.set(f"Added '{text}'")

    def clear_list(self) -> None:
        self.listbox.delete(0, "end")
        self.status_var.set("List cleared")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
