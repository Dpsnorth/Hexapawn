from tkinter import *
from tkinter import messagebox
import pickle
import os

window=Tk()
window.geometry("500x500")

rules='''Hexapawn is a two-player board game invented by Martin Gardner.
It is played on a 3x3 board with each player given 3 pawn pieces.
To win a round a player must either reach the oposite side of the
gameboard or trap their opponents pieces by preventing them from performing
a legal move. The rules are similar to a mini game of chess – using
only pawns. A piece can move forward one square only if that square is empty.
You can take an opponent's piece if it is in a diagonally neighbouring
square – just like a pawn attack in chess. The players take turns to move their pieces,
starting with White.'''

RulesHead=Label(text="Rules")
RulesHead.config(font=("Courier",20,'bold'))
rulelabel=Label(text=rules)

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

StartGame.place(relx=0.4, rely=0.5, anchor=CENTER)
Scores.place(relx=0.6, rely=0.5, anchor=CENTER)

RulesHead.place(relx=0.5, rely=0.075, anchor=CENTER)
rulelabel.place(relx=0.5, rely=0.25, anchor=CENTER)
window.mainloop()
