import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext
host = '127.0.0.1'
port = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
class ChatClient:
    def __init__(self, master):
        self.master = master
        master.title("Chat Client")
        self.chat_area = scrolledtext.ScrolledText(master)
        self.chat_area.pack(fill='both', expand=True)
        self.chat_area.config(state='disabled')
        self.msg_entry = tk.Entry(master)
        self.msg_entry.pack(fill='x')
        self.msg_entry.bind("<Return>", self.send_message)
        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname:", parent=master)
        client.send(self.nickname.encode('utf-8'))
        threading.Thread(target=self.receive_messages, daemon=True).start()
    def receive_messages(self):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.chat_area.config(state='normal')
                self.chat_area.insert('end', message + '\n')
                self.chat_area.yview('end')
                self.chat_area.config(state='disabled')
            except:
                client.close()
                break
    def send_message(self, event):
        msg = self.msg_entry.get()
        if msg:
            client.send(f"{self.nickname}: {msg}".encode('utf-8'))
            self.msg_entry.delete(0, 'end')
root = tk.Tk()
app = ChatClient(root)
root.mainloop()
