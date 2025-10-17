import socket
import tkinter as tk
from tkinter import scrolledtext

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# --- GUI SETUP ---
window = tk.Tk()
window.title("TCP Client")

chat_area = scrolledtext.ScrolledText(window, width=50, height=10, state='disabled')
chat_area.pack(padx=10, pady=10)

msg_entry = tk.Entry(window, width=40)
msg_entry.pack(side=tk.LEFT, padx=10)

def send_message():
    msg = msg_entry.get()
    if msg:
        client.send(msg.encode())
        if msg.lower() == 'exit':
            window.destroy()
            client.close()
            return
        response = client.recv(1024).decode()
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f"You: {msg}\nServer: {response}\n\n")
        chat_area.config(state='disabled')
        msg_entry.yview( tk.END)

send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

window.mainloop()
client.close()
