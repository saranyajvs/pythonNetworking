import socket
from tkinter import *


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', 'Server: ' + message)
    entry.delete(0, END)
    client.send(bytes(message, 'utf-8'))


def recieve(listbox):
    client_message = client.recv(100)
    listbox.insert('end', 'Client:' + client_message.decode("utf-8"))


root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()

button = Button(root, text='Send', command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text='Receive', command=lambda: recieve(listbox))
rbutton.pack(side=BOTTOM)
root.title('Server')
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
port = 12345
sockt.bind((host_name, port))
sockt.listen(4)

client, address = sockt.accept()
# while True:
#     message = input("server: ")
#     client.send(bytes(message, 'utf-8'))
# client_message = client.recv(100)
# # print('client is connected and has the IP:', address)
# print("client :" + client_message.decode("utf-8"))
root.mainloop()
