#import de libraries die gebruikt worden
import datetime
import time
import tkinter as tk
import threading
import winsound
import sys

root = tk.Tk()

#maakt functie aan die chekt of er is iets ingezet is

def wekkerZetten():
    #haalt nummers uit de twee textvelden en formatteert het
    tijd = f"{entry1.get()}:{entry2.get()}"
   
    if tijd !=  ":":
        #zo ja, stuur tijd door naar de wekkerGaat() functie 
        wekkerGaat(tijd)
    else:
        print("AUB opnieuw opstarten")

#functie de de wekker laat afgaan
def wekkerGaat(tijd):
    while True:
        #voert alles uit in de while loop 1x per seconde
        time.sleep(1)
        #huidigeTijd variabel wordt de huidige tijd in uren en minuten gezet in een string
        huidigeTijd = datetime.datetime.now().strftime("%H:%M")
        print(huidigeTijd)
        #Als de tijd gelijk is aan de huidige tijd gaat de wekker af en gaat daarna uit de for loop
        if huidigeTijd == tijd:
            text = tk.Label(frame2, text="wakker worden!!!!", bg="green", font=("comic_sans", 30))
            text.place(relx=0, rely=0.25)
            winsound.PlaySound("SystemStart", winsound.SND_ALIAS)
            break

#Constants voor de window grootte wanneer je het opstart.
HEIGHT = 300
WIDTH = 400
#Maakt de GUI met twee frames, 2 textfields, 1 button met de event dat die wekkerZetten() gaat doen met threading.                                                                                     
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame1 = tk.Frame(root, bg='#B86E5E')
frame1.place(relx=0.1, rely=0.1, relwidth=0.40, relheight=0.40)

frame2 = tk.Frame(root, bg='green')
frame2.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)

entry1 = tk.Entry(frame1)
entry1.place(relx=0.05, rely=0.45, relwidth=0.40)

entry2 = tk.Entry(frame1)
entry2.place(relx=0.95, rely=0.45, relwidth=0.40, anchor='ne')

button = tk.Button(root, text="s\ne\nt \nt\ni\nm\ne", command=threading.Thread(target=wekkerZetten, daemon=True).start)
button.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.40)

root.mainloop()
