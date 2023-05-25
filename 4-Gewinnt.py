from tkinter import *
from array import * 
import tkinter.messagebox

root = Tk()

spielfeld = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

color= ["red"]
counter = 0
gewinncounter = 0

movecounters = [0, 0, 0, 0, 0, 0, 0, 0]

# min feldgröße 
root.minsize(width=750, height=600)

# Größe des Fensters beim öffnen 
canvas = Canvas(root, height=600, width=750)
canvas.pack()

# Hintergrundfläche
canvas.create_rectangle(190,95,560,420, fill="blue")

# Kreise machen
for i in range (6):
    for u in range(7):
        canvas.create_oval((u+1)*50+150,(i+1)*50+50,(u+1)*50+200,(i+1)*50+100, fill="white")

# vertikale Linien 
for i in range (6):
    canvas.create_line((i+1)*50+200,100,(i+1)*50+200,400,width = 3,fill="blue")

# horizontale Linien 
for i in range (5):
    canvas.create_line(200,(i+1)*50+100,550,(i+1)*50+100,width = 3,fill="blue")

# Ausenlinien
canvas.create_line(190,95,190,461,width=8)
canvas.create_line(560,95,560,461,width=8)
canvas.create_line(186,420,564,420,width=8)

# Dreiecke unten 
canvas.create_polygon(186, 420, 186, 460, 150, 460, fill="blue", outline="black", width=2)
canvas.create_polygon(564, 420, 564, 460, 600, 460, fill="blue", outline="black", width=2)


#-----------------------------------------------CODE------------------------------------------------

def key(event=NONE):
    global movecounters, color

    # Prüft das Zahl zwischen 1 - 7
    if event.char.isdigit() and int(event.char) >= 1 and int(event.char) <= 7:
        for i in range(7):

            # Ändert nach jedem durchgang die Farbe
            if color == "red":
                color = "red"
            else:
                color = "yellow"
            
            # erzeugt den Kreis an der Gewünschten stelle 
            if int(event.char) == i+1:
                if int(movecounters[i+1]) < 6:
                    canvas.create_oval((i+1)*50+150,350-int(movecounters[i+1])*50,(i+1)*50+200,400-int(movecounters[i+1])*50,fill=color,
                                  outline = "black", width = 2)
                    movecounters[i+1] = movecounters[i+1] + 1
 
                    if color =="red":
                        color = "yellow"
                    else:
                        color = "red"

                # erhöht denn "movecounters" über 6. -> Zur Prüfung ob die Zeile voll ist  
                else:
                    movecounters[i+1] = movecounters[i+1] + 1

    matrix(event)
    Pruefung(event)
    return movecounters



def matrix (event=NONE):
    global counter, spielfeld, movecounters

    # Prüft das Zahl zwischen 1 - 7
    if event.char.isdigit() and int(event.char) >= 1 and int(event.char) <= 7:                      
        for w in range (1,8):
            
            # befüllt die Matrix mit der 2 
            if int(event.char) == w and counter % 2 != 0 and movecounters[int(event.char)] < 7:
                        spielfeld[(-1)*int(movecounters[int(event.char)])][w-1] = 2       # rot

                        # gibt die Matrix aus 
                        for r in spielfeld:
                                print(r)
                                print()
                        counter = counter + 1
                        print()

            # befüllt die Matrix mit der 1            
            elif int(event.char) == w and counter % 2 == 0 and movecounters[int(event.char)] < 7:
                        spielfeld[(-1)*int(movecounters[int(event.char)])][w-1] = 1       # gelb

                        # gibt die Matrix aus 
                        for r in spielfeld:
                                print(r)
                                print()
                        counter = counter + 1
                        print()

            # Prüft ob die Zeile voll ist 
            elif movecounters[int(event.char)] > 6:
                tkinter.messagebox.showinfo("Fehler", "Die Zeile ist voll")
                break

    # gibt eine Fehlermeldung wenn die Zahl nicht zwischen 1 - 7 ist 
    else:
        tkinter.messagebox.showinfo("Fehler", "Falsche Eingabe")
            
        return spielfeld



def Pruefung (event=NONE):
    global movecounters, spielfeld, gewinncounter

    # Prüft auf gelb (0) und rot (1) 
    for c in range(2):
        
        # vertikale Prüfung 
        for i in range (6):
            for u in range (7):
                if spielfeld[i][u] == c+1:
                    gewinncounter = gewinncounter + 1                       
                else:
                    gewinncounter = 0
                    
                if gewinncounter == 4 and c == 0: 
                    tkinter.messagebox.showinfo("Jo", "Gelb hat Gewonnen")
                    break
                elif gewinncounter == 4 and c == 1:
                    tkinter.messagebox.showinfo("Jo", "Rot hat Gewonnen")
                    break

            # da im letztem Durchgang der schleife der gewinncounter nicht zurückgesetzt 
            gewinncounter = 0

        # horizontale Prüfung
        for i in range (7):
            for u in range (6):
                if spielfeld[u][i] == c+1:
                    gewinncounter = gewinncounter + 1
                else:
                    gewinncounter = 0 
                    
                if gewinncounter == 4 and c == 0: 
                    tkinter.messagebox.showinfo("Jo", "Gelb hat Gewonnen")
                    break
                elif gewinncounter == 4 and c == 1:
                    tkinter.messagebox.showinfo("Jo", "Rot hat Gewonnen")
                    break
            gewinncounter = 0

        # diagonale Prüfung Links -> Rechts mit änderung nach unten       
        for i in range(3):

            # damit [u+i] maximal 6 ist 
            for u in range (6-i):
                
                # u+i damit die reihe um eins nach unten verschoben wird 
                if spielfeld[u+i][u] == c+1:
                    gewinncounter = gewinncounter + 1      
                else:
                    gewinncounter = 0
                    
                if gewinncounter == 4 and c == 0: 
                    tkinter.messagebox.showinfo("Jo", "Gelb hat Gewonnen")
                    break
                elif gewinncounter == 4 and c == 1:
                    tkinter.messagebox.showinfo("Jo", "Rot hat Gewonnen")
                    break
            gewinncounter = 0


        # diagonale Prüfung Links -> Rechts mit änderung nach rechts; (1,4) damit nicht 2 mal die Links -> Rechts Diagonale geprüft wird
        for i in range (1,4):
            for u in range (7-i):

                # u+i damit die reihe um eins nach rechts verschoben wird 
                if spielfeld[u][u+i] == c+1:
                    gewinncounter = gewinncounter + 1   
                else:
                    gewinncounter = 0
                    
                if gewinncounter == 4 and c == 0: 
                    tkinter.messagebox.showinfo("Jo", "Gelb hat Gewonnen")
                    break
                elif gewinncounter == 4 and c == 1:
                    tkinter.messagebox.showinfo("Jo", "Rot hat Gewonnen")
                    break
            gewinncounter = 0

        # diagonale Prüfung Rechts -> Links mit änderung nach unten
        for i in range (3):
            for u in range (6-i):
                
                #[6-u] damit von der rechten seite aus gegangen wird 
                if spielfeld[u+i][6-u] == c+1:
                    gewinncounter = gewinncounter + 1  
                else:
                    gewinncounter = 0
                    
                if gewinncounter == 4 and c == 0: 
                    tkinter.messagebox.showinfo("Jo", "Gelb hat Gewonnen")
                    break
                elif gewinncounter == 4 and c == 1:
                    tkinter.messagebox.showinfo("Jo", "Rot hat Gewonnen")
                    break
            gewinncounter = 0
              
        # diagonale Prüfung Rechts -> Links mit änderung nach links
        for i in range (1,4):
            for u in range (7-i):
                
                #[(5-i)-u] damit die Spalte maximal 5 (keine wiederholung der Diagonalen) und durch u immer weniger wird 
                if spielfeld[u][(6-i)-u] == c+1:
                    gewinncounter = gewinncounter + 1

                else:
                    gewinncounter = 0
                                    
                if gewinncounter == 4 and c == 0: 
                    tkinter.messagebox.showinfo("Jo", "Gelb hat Gewonnen")
                    break
                elif gewinncounter == 4 and c == 1:
                    tkinter.messagebox.showinfo("Jo", "Rot hat Gewonnen")
                    break
            gewinncounter = 0

    # wenn alle Felder ohne einen Gewinner befühlt sind   
    if counter == 42:
        tkinter.messagebox.showinfo("Jo", "Unentschieden")


root.bind("<Key>", key)
root.mainloop()


