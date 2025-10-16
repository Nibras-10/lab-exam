import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

HOST, PORT = '127.0.0.1', 12345

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.window = tk.Tk()
        self.window.title("TCP Chat Client")

        # Chat display
        self.chat_box = scrolledtext.ScrolledText(self.window, state='disabled', width=60, height=20)
        self.chat_box.pack(padx=10, pady=5)

        # Message entry
        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack(padx=10, pady=5, side=tk.LEFT)
        self.entry.bind("<Return>", self.send_msg)

        tk.Button(self.window, text="Send", command=self.send_msg).pack(side=tk.LEFT, padx=5)

        # Username prompt
        self.username = simpledialog.askstring("Username", "Enter username:", parent=self.window)
        if not self.username:
            messagebox.showerror("Error", "Username required!")
            self.window.quit()
            return

        # Connect to server
        try:
            self.client.connect((HOST, PORT))
            if self.client.recv(1024).decode() == "USERNAME":
                self.client.send(self.username.encode())
        except:
            messagebox.showerror("Connection Error", "Unable to connect to server.")
            self.window.quit()
            return

        # Start receiver thread
        self.running = True
        threading.Thread(target=self.receive, daemon=True).start()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()

    def send_msg(self, event=None):
        msg = self.entry.get().strip()
        if not msg:
            return
        full = f"{self.username}: {msg}"
        self.client.send(full.encode())

        # Display locally
        self.update_chat(full)
        self.entry.delete(0, tk.END)

    def receive(self):
        while self.running:
            try:
                msg = self.client.recv(1024).decode()
                self.update_chat(msg)
            except:
                break

    def update_chat(self, msg):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, msg + "\n")
        self.chat_box.config(state='disabled')
        self.chat_box.yview(tk.END)

    def close(self):
        self.running = False
        try:
            self.client.close()
        except:
            pass
        self.window.destroy()

if __name__ == "__main__":
    ChatClient()
