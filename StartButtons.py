from tkinter import *
from tkinter import messagebox
import pickle
import os

window=Tk()
window.geometry("400x400")

def RunFile():
    os.system("main.py")

def CurrentScore():
    try:
        fh=open(r"Scores.dat","rb+")
        WinLoose=pickle.load(fh)
        fh.close()
        Wins=WinLoose['Wins']
        Losses=str(WinLoose['Losses'])
        str1="Games Won : "+str(Wins)+"\nGames Lost : "+str(Losses)
        messagebox.showinfo("Scores",str1)
    except FileNotFoundError:
        messagebox.showinfo("Scores","No scores available")

StartGame=Button(window,text="Start Game",command=RunFile,height=2,width=10)
Scores=Button(window,text="Scores",command=CurrentScore,height=2,width=10)  

StartGame.place(relx=0.5, rely=0.4, anchor=CENTER)
Scores.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()
