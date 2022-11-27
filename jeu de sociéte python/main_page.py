
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter


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

def connexion():
    player_name = name_input.get()
    player_ip = ip_input.get()
    player_port = port_input.get()
    print("Phase de connexion avec\n"+str(player_name)+"\n"+str(player_ip)+"\n"+str(player_port))

    connexion_button.configure(text="Connexion")

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

#affichage des erreurs
def port_incorrect() :
    port_input.delete(0, END)
    port_input.insert(0,"le port est incorrect")

def ip_incorrect() :
    ip_input.delete(0, END)
    ip_input.insert(0,"L'ip est incorrect") 

def all_incorrect() :
    player_name = name_input.get()
    player_ip = ip_input.get()
    player_port = port_input.get()
    if player_name == "" :
        name_input.delete(0, END)
        name_input.insert(0,"Votre Pseudo")
    if player_ip == "" :
        ip_input.delete(0, END)
        ip_input.insert(0,"L'ip de connexion")
    ip_verif()
    if player_port == "" :
        port_input.delete(0, END)
        port_input.insert(0,"le port de connexion")
    port_verif()


#vérification ip et port correct
    #port verif
def port_verif():
    player_port = port_input.get()
    verif_port = player_port
    verif_port = verif_port.replace(".", "0")
    if verif_port.isdigit() == True and int(player_port) <= 65535 and int(player_port) > 1024 :
        connexion()
            
    else :
        #print("le port est incorrect")
        port_incorrect()
    #ip verif

def ip_verif():
    player_ip = ip_input.get()
    verif_ip = player_ip
    verif_ip = verif_ip.replace(".", "0")
    if player_ip.count(".") > 0 and verif_ip.isdigit() == True:
        return
    else :
        #print("L'ip est incorrect")
        ip_incorrect()




#get entry box
    #get name, ip, port
def click_action_joindre():
    #vérification input

    player_name = name_input.get()
    player_ip = ip_input.get()
    player_port = port_input.get()

    if player_name == "" or player_name == "Votre Pseudo" or player_ip == "" or player_ip == "L'ip de connexion" or player_port == "" or player_port == "le port de connexion" :
        #print("Veuillez entrer votre pseudo, une ip ou un port correct.")
        all_incorrect()
        return

    ip_verif()
    port_verif()
    return
    #end


#setup de la page

win.title("loup Garou")
win.geometry("1600x900")
#win.minsize(1600, 900)
win.iconbitmap("images\logo.ico")
win.config(background=color_background)



#creer une boite
frame = Frame(win, bg=color_background)

sous_frame1 = Frame(frame, bg=color_background)
sous_frame2 = Frame(frame, bg=color_background)
button_frame = Frame(sous_frame2, bg=color_background)



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
name_input.insert(0,"Votre Pseudo")
name_input.config()
name_input.bind("<Button-1>", click_name)
name_input.pack(pady=5, ipady=10)

    #ip
ip_input = Entry(sous_frame2, justify=CENTER, textvariable=player_ip, font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
ip_input.insert(0,"L'ip de connexion")
ip_input.config()
ip_input.bind("<Button-1>", click_ip)
ip_input.pack(pady=5, ipady=10)

    #port
port_input = Entry(sous_frame2, justify=CENTER, textvariable=player_port, font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
port_input.insert(0,"le port de connexion")
port_input.config()
port_input.bind("<Button-1>", click_port)
port_input.pack(pady=5, ipady=10)

    #end

# bouton
connexion_button = Button(button_frame, text="Rejoindre", font=("Segoe UI Black", 25), bg=color_background, fg="#03090D", command=click_action_joindre, relief=SOLID, bd=1, width=15)
connexion_button.pack()

# ajouter
frame.pack(expand=YES)
sous_frame1.pack(expand=YES, pady=50)
sous_frame2.pack(expand=YES)
button_frame.pack(expand=YES, pady=30)


#affichage
win.mainloop()