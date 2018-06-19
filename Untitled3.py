import sys
import fileinput
import random
from tkinter import *

def LeesTaak():
    print("\nDit zijn uw opgeslagen taken: ")
    with open('text.txt', "r") as file:
        zinnen = file.readlines()
    for count, item in enumerate(zinnen, start = 1):
        ct = str(count) + '.'
        print(ct, item)
    
def ToevoegenTaak(taak):
    with open('text.txt', "a") as file:
        file.write(taak + '\n')
    print("\nUw taak is toegevoegd.\n")
    
def VerwijderTaak(taak):
    gevonden = []
    with open('text.txt', "r") as file:
        lijst = file.readlines()
    while taak+'\n' in lijst:
        lijst.remove(taak+'\n')
    with open('text.txt', "w") as file:
        file.write(''.join(lijst))
    print("\nDe taak is verwijderd.\n")
    
def Gegevens():
    keuze = ''
    while keuze != 'e':
        keuze = input("Welkom bij de file editor.\nDruk 1 om uw lijst te zien.\nDruk 2 om een taak toe te voegen.\nDruk 3 om een taak te verwijderen.\nDruk 'e' om weg te gaan.\nWat wilt u doen? ")
        if keuze == '1':
            LeesTaak()
        elif keuze == '2':
            taak = input("Wat wilt u toevoegen?")
            ToevoegenTaak(taak)
        elif keuze == '3':
            taak = input("Welke taak wilt u verwijderen?")
            VerwijderTaak(taak)
        elif keuze == 'e':
            print("Terug naar het hoofdmenu!\n\n")
        else:
            print("Geen geldige optie")    



#Gegevens()
def p_b(array):
    for i in range(3):
        print(' '.join(array[i]))
    print("\n")
def invoer1(int, array):
    if int == "1":
        array[0][0] = " O "
    elif int == "2":
        array[0][1] = " O "
    elif int == "3":
        array[0][2] = " O "
    elif int == "4":
        array[1][0] = " O "
    elif int == "5":
        array[1][1] = " O "
    elif int == "6":
        array[1][2] = " O "
    elif int == "7":
        array[2][0] = " O "
    elif int == "8":
        array[2][1] = " O "
    elif int == "9":
        array[2][2] = " O "
    return(array)

def invoer2(int, array):
    if int == "1":
        array[0][0] = " X "
    elif int == "2":
        array[0][1] = " X "
    elif int == "3":
        array[0][2] = " X "
    elif int == "4":
        array[1][0] = " X "
    elif int == "5":
        array[1][1] = " X "
    elif int == "6":
        array[1][2] = " X "
    elif int == "7":
        array[2][0] = " X "
    elif int == "8":
        array[2][1] = " X "
    elif int == "9":
        array[2][2] = " X "
    return(array)

def check_winnaar(array):
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2] == " O ":
            print("Gefeliciteerd Speler 1!")
            return(False)
        elif array[i][0] == array[i][1] == array[i][2] == " X ":
            print("Gefeliciteerd Speler 2.")
            return(False)
        elif array[0][i] == array[1][i] == array[2][i] == " O ":
            print("Gefeliciteerd Speler 1!")
            return(False)
        elif array[0][i] == array[1][i] == array[2][i] == " X ":
            print("Gefeliciteerd Speler 2.")
            return(False)
        elif array[0][0] == array[1][1] == array[2][2] == " O ":
            print("Gefeliciteerd Speler 1!")
            return(False)
        elif array[0][0] == array[1][1] == array[2][2] == " X ":
            print("Gefeliciteerd Speler 2.")
            return(False)
        elif array[0][2] == array[1][1] == array[2][0] == " O ":
            print("Gefeliciteerd Speler 1!")
            return(False)
        elif array[0][2] == array[1][1] == array[2][0] == " X ":
            print("Gefeliciteerd Speler 2.")
            return(False)
        else:
            return(True)


def invoerfunctie(prompt, lijst):
    while True:
            try:
                invoerO = input(prompt)
            except ValueError:
                print("Hmmm, wanneer gebeurt dit nou?")
                continue
            
            if invoerO not in lijst:
                print("Geen geldige invoer.\n")
                continue
            else:
                return(invoerO)
                break

def Ttt():
    up = ["-1-", "-2-","-3-"]
    mid = ["-4-", "-5-","-6-"]
    low = ["-7-", "-8-","-9-"]
    bord = [up, mid, low]
    print("Welkom bij Tic Tac Toe!")
    p_b(bord)
    Doorgaan = True
    lijst = ["1","2","3","4","5","6","7","8","9"]
    while Doorgaan == True:
        invoerO = invoerfunctie("Wat wil je doen Speler 1: ", lijst)
        lijst.remove(invoerO)
        bord = invoer1(invoerO, bord)
        p_b(bord)
        Doorgaan = check_winnaar(bord)
        if Doorgaan == False:
            break;
        elif lijst == []:
            print("Oh, er was geen winnaar.")
            break;
        
        invoerX = invoerfunctie("Wat wil je doen Speler 2: ",lijst)
        lijst.remove(invoerX)
        bord = invoer2(invoerX, bord)
        p_b(bord)
        Doorgaan = check_winnaar(bord)
        if lijst == []:
            print("Oh, niemand heeft gewonnen. Jammer!")
            break;
    print("Bedankt voor het spelen. Terug naar het hoofdmenu!\n\n")
    
def main():
    lijst = ["1", "2", "e"]
    print("Welkom bij mijn idiote programma.\n")
    invoer = "1"
    while invoer != "e":
        print("Hoofdmenu.\nDruk 1 voor de file editor;\nDruk 2 voor TTT;\nDruk e om te stoppen.\n")
        invoer = invoerfunctie("Kies maar: ", lijst)
        if invoer == "1":
            print("\n\n")
            Gegevens()
        elif invoer == "2":
            print("\n\n")
            Ttt()
        elif invoer == "e":
            break
    print("Tot ziens!")
        
main()