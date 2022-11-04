#!/usr/bin/env python
# coding: utf-8
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Schere-Stein-papier" data-toc-modified-id="Schere-Stein-papier-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Schere Stein papier</a></span></li></ul></div>
# ### Schere Stein papier
import random
print("Spiele Schere-Stein-Papier mit mir!")
print("Bitte wähle: Schere (0), Stein (1) oder Papier (2)")
print("Um das Spiel zu beenden, schreibe: End")
Handzeichen = [0, 1, 2]
while True:
    Eingabe = input("Deine Wahl: ")
    if Eingabe == "End":
        break
        
    Eingabe = int(Eingabe)
    random.shuffle(Handzeichen)
    Computer = Handzeichen[0]
    
    print("Computer: " + str(Computer))
    
    if Computer == (Eingabe)%3:
        print("Unentschieden!")
    elif Computer == (Eingabe + 1)%3:
        print("Du hast verloren!")
    elif Computer == (Eingabe + 2)%3:
        print("Du hast gewonnen!")
help(random.shuffle)
