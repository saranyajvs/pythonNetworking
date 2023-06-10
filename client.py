import socket
from tkinter import *


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', message)
    entry.delete(0, END)
    sockt.send(bytes(message, 'utf-8'))
    recieve(listbox)


def recieve(listbox):
    message = sockt.recv(100)
    listbox.insert('end','Server: '+ message.decode("utf-8"))


root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()

button = Button(root, text='Send', command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)
rbutton = Button(root, text='Receive', command=lambda: recieve(listbox))
rbutton.pack(side=BOTTOM)
root.title('Client')
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
port = 12345
sockt.connect((host_name, port))
root.mainloop()
# while True:
#     msg = sockt.recv(100)
#     print("server:" + msg.decode('utf-8'))
#     message_to_server = input("Client:")
    # sockt.send(bytes(message_to_server,'utf-8'))
    ## print(msg.decode('utf-8'))
