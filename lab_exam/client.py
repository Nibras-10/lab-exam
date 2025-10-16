import socket
import tkinter as tk
from tkinter import messagebox, scrolledtext

HOST = '127.0.0.1'
PORT = 65432

def send_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return
    
    client.send(text.encode())
    response = client.recv(1024).decode()
    output_area.config(state='normal')
    output_area.delete('1.0', tk.END)
    output_area.insert(tk.END, response)
    output_area.config(state='disabled')

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# GUI setup
root = tk.Tk()
root.title("Palindrome Client")

tk.Label(root, text="Enter text:").pack()
text_input = scrolledtext.ScrolledText(root, width=50, height=5)
text_input.pack()

tk.Button(root, text="Send to Server", command=send_text).pack(pady=10)

tk.Label(root, text="Server Response:").pack()
output_area = scrolledtext.ScrolledText(root, width=50, height=5, state='disabled')
output_area.pack()

root.mainloop()
client.close()
