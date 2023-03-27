# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from random import randint
# On crée un environnement Tkinter
tk = Tk()


def right(event):
    global direction
    direction='right'
    
def left(event):
    global direction
    direction='left'

def up(event):
    global direction
    direction='up'

def down(event):
    global direction
    direction='down'

def computeNextFrame(numFrame,coordonnee):
    global direction
    numFrame=numFrame+1
    can.delete('all')    

#effacer le canavas
    can.delete('all')
#pragramation du deplacement des noeuds
    for n in range(len(coordonnee)-1, 0, -1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]

# Mise à jour des coordonnées
    if direction == 'right':
        coordonnee[0] += 20
        if coordonnee[0] > 500:
            coordonnee[0] = 0
    if direction == 'left':
        coordonnee[0] += -20
        if coordonnee[0] < 0:
            coordonnee[0] = 480
    if direction == 'up':
        coordonnee[1] += -20
        if coordonnee[1] < 0:
            coordonnee[1] = 480
    if direction == 'down':
        coordonnee[1] += 20
        if coordonnee[1] > 500:
            coordonnee[1] = 0
#creer le corp du serpent
    can.create_rectangle(coordonnee[0], coordonnee[1], coordonnee[0] + 20,coordonnee[1] + 20, outline='yellow', fill='red')
    
    for n in  range (1,len(coordonnee)):
        can.create_recteangle(coordonnee[n][0],coordonnee[n][1],coordonnee[n][0] + 20,
                              coordonnee[n][1]+20, outline='blue',fill='green')
    tk.after(100,lambda:computeNextFrame(numFrame,coordonnee))

    can = Canvas(tk, width=500, height=500, bg='black')
# On affiche le canevas
    can.pack()
#direction par defaut
    direction= 'up'

    coordonnee = [[200,200], [200,220], [200,240], [200,240]]
    objet=[]

#premier objet (la pomme)
    x= randint(1,24)
    y= randint(1,24)
    objet.append([x*20, y*20, 0])

computeNextFrame(0,[200,200])

tk.bind('<d>',right)
tk.bind('<z>',up)
tk.bind('<q>',left)
tk.bind('<s>',down)
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas

"""
can.create_rectangle(500,0,480,20,outline='yellow',fill='green')
can.create_oval(100,200,120,120,outline='red',fill='blue')
"""
# lancement de la boucle principale qui écoute les évènements (claviers...)
tk.mainloop() # Cet appel doit être la derniere instruction du programme





