import socket
from tkinter import *

def send(listv, entry):
    message = entry.get()
    listv.insert(END,"Client : " +message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    receive(listv)

def receive(listv):
    message = s.recv(50)
    listv.insert(END,"Server : "+message.decode("utf-8"))

root = Tk()

entry = Entry()
entry.pack(side = BOTTOM)

listv = Listbox(root)
listv.pack()

button = Button(root, text = "Send", command = lambda: send(listv, entry))
button.pack(side = BOTTOM)

rbutton = Button(root, text = "Receive", command = lambda: receive(listv))
rbutton.pack(side = BOTTOM)

root.title("Client")
root.geometry("300x300")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

root.mainloop()
    
 