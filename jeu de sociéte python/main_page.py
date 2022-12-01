import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter
import time

import socket


#fenêtre 

win = tk.Tk()


#variable
    #
    # #081621
    # #0C2233
color_background ="#0C2233"
    #input variable
player_name = ""
player_ip = ""
player_port = ""


#connection au hub avec toute les verif
#text input placeholder
    #name
def click_name(event):

    name_input.config(state=NORMAL)
    name_input.delete(0, END)
    #ip
def click_ip(event):

    ip_input.config(state=NORMAL)
    ip_input.delete(0, END)
    #port
def click_port(event):

    port_input.config(state=NORMAL)
    port_input.delete(0, END)
    #end

#button press action run --->
def click_action_joindre():

    player_name = name_input.get()
    player_ip = ip_input.get()
    player_port = port_input.get()
    print(player_name+" "+player_ip+" "+player_port)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((str(player_ip),int(player_port)))

    #send data
    data = str(player_name)+" "+str(player_ip)+" "+str(player_port)
    clientSocket.send(data.encode())

    #recive data
    dataFromServer = clientSocket.recv(1024)
    print(dataFromServer.decode())

    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((str(player_ip),int(player_port)))
    data = str(player_name)+" rôle "+str("loup_garou")
    clientSocket.send(data.encode())

    dataFromServer = clientSocket.recv(1024)
    print(dataFromServer.decode())






#setup de la page

win.title("loup Garou")
win.geometry("1600x900")
#win.minsize(1600, 900)
win.iconbitmap("images\logo.ico")
win.config(background=color_background)



#creer une boite
frame = Frame(win, bg="#f2654b")
frame = Frame(win, bg=color_background)

sous_frame1 = Frame(frame, bg=color_background)
sous_frame2 = Frame(frame, bg=color_background)
button_frame = Frame(sous_frame2, bg=color_background)

#texte
label_title = Label(frame, text="Secret Hilter", font=("Impact", 40), bg="#f2654b", fg="white")


#texte/logo
    #Logo image
image_logo = Image.open("images\logo.png")
test = ImageTk.PhotoImage(image_logo)
label_logo = Label(sous_frame1, text="Logo jeu", bg=color_background, image=test)
label_logo.pack()
    #texte
label_title = Label(sous_frame1, text="Loup Garou", font=("Impact", 40), bg=color_background, fg="#03090D")
label_title.pack()
    #end

#text input
    #name
name_input = Entry(sous_frame2, justify=CENTER, textvariable=player_name , font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
#name_input.insert(0,"Votre Pseudo")
name_input.insert(0,"OelectronO")
name_input.config()
name_input.bind("<Button-1>", click_name)
name_input.pack(pady=5, ipady=10)

    #ip
ip_input = Entry(sous_frame2, justify=CENTER, textvariable=player_ip, font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
#ip_input.insert(0,"L'ip de connexion")
ip_input.insert(0,"192.168.1.29")
ip_input.config()
ip_input.bind("<Button-1>", click_ip)
ip_input.pack(pady=5, ipady=10)

    #port
port_input = Entry(sous_frame2, justify=CENTER, textvariable=player_port, font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
#port_input.insert(0,"le port de connexion")
port_input.insert(0,"5456")
port_input.config()
port_input.bind("<Button-1>", click_port)
port_input.pack(pady=5, ipady=10)

    #end

# bouton
connexion_button = Button(button_frame, text="Rejoindre", font=("Segoe UI Black", 25), bg=color_background, fg="#03090D", activebackground=color_background, activeforeground="#03090D" ,command=click_action_joindre, relief=SOLID, bd=1, width=15)
connexion_button.pack()

# ajouter
frame.pack(expand=YES)
sous_frame1.pack(expand=YES, pady=50)
sous_frame2.pack(expand=YES)
button_frame.pack(expand=YES, pady=30)



#affichage

def click_action_joindre() :
    global player_name, player_ip, player_port
    print(player_name+" "+player_ip+" "+player_port)

win.mainloop()