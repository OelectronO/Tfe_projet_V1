
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter
import webbrowser


def open_rules():
    webbrowser.open_new("https://reglesdejeux.github.io/regles-du-jeu-secret-hitler/index.html")

#fenêtre 

win = tk.Tk()


#setup de la page

win.title("Secret Hitler")
win.geometry("1600x900")
win.minsize(1600, 900)
win.iconbitmap("logo.ico")
win.config(background="#f2654b")

#creer une boite
frame = Frame(win, bg="#f2654b")

#texte
label_title = Label(frame, text="Secret Hilter", font=("Impact", 40), bg="#f2654b", fg="white")
label_title.pack()

#second texte
label_subtitle = Label(frame, text="slt", font=("Impact", 25), bg="#f2654b", fg="white")
label_subtitle.pack()

# bouton
test_button = Button(frame, text="Bonjour", font=("Impact", 25), bg="white", fg="#f2654b", command=open_rules)
test_button.pack(pady=25, fill=X)

# ajouter
frame.pack(expand=YES)

#affichage
win.mainloop()