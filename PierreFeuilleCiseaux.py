#pierre feuille ciseaux

#start game

start = str(input("Commencer le jeux (ecrivez ok) : "))

while start != "ok":
    start = str(input("Commencer le jeux (ecrivez ok) : "))


#créer le tirage random de l ordinateur

import random

LIST = ("pierre","feuille","ciseaux")
list = random.choice(LIST)

#faire le jeu

play = str(input("pierre,feuille,ciseaux ... : "))

if list == "pierre" :
    if play == "ciseaux":
        print(list)
        print("perdu")
    if play == "pierre":
        print(list)
        print("egalité")
    if play == "feuille":
        print(list)
        print("gagné")

elif list == "feuille" :
    if play == "pierre":
        print(list) 
        print("perdu")
    if play == "feuille":
        print(list)
        print("egalité")
    if play == "ciseaux":
        print(list)
        print("gagné")

elif list == "ciseaux":
    if play == "feuille":
        print(list) 
        print("perdu")
    if play == "ciseaux":
        print(list)
        print("égalité")
    if play == "pierre":
        print(list)
        print("gagné")
