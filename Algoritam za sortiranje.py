import pygame as pg
import random
pg.init()

(sirina, visina) = (1080, 540)
global sirinasred
global visinasred
(sirinasred, visinasred) = (int(sirina / 2), int(visina / 2))
    
prozor = pg.display.set_mode((sirina,visina))
prozor.fill((255,255,255))

global dugmesir
global dugmevis
(dugmesir, dugmevis) = (300, 150)

pg.draw.rect(prozor,(50,50,200),(int(sirinasred - dugmesir), int(visinasred - dugmevis), int(dugmesir) , int(dugmevis)))

pg.display.update()

def bubblesort():
    #kreiranje liste i random elemenata
    brojelemenata = int(input("Koliko elemenata imamo?")) #unos koliko elemenata
    lst = [] 

    for i in range(0,brojelemenata,1):
        rand = random.randint(10,500) #random od 10 do 500
        lst.append(rand) 

    print("ELEMENTI:")
    for i in range(0,brojelemenata,1):
        print(lst[i])

    #razdvajanje u ispisu
    print("------")
    print("SORTIRANO:")

    #bubble sort
    for j in range(brojelemenata): 
        for i in range(0,brojelemenata-1,1):
            if lst[i] > lst[i+1]:
                t = lst[i] #t = temporary da skladisti vrednost promenljive
                lst[i] = lst[i+1]
                lst[i+1] = t

    for i in range(0,brojelemenata,1):
        print(lst[i])

#glavna funkcija za dugme:

def dugme():
    inbox = False #inbox - proverava da li je mis unutar dugmeta
    event = pg.event.wait()
    
    if event.type == pg.MOUSEMOTION or event.type == pg.MOUSEBUTTONDOWN:
        pozmisa = pg.mouse.get_pos() #kada se klikne ili pomeri mis pronadje se pozicija
        
        if sirinasred > pozmisa[0] > sirinasred - dugmesir and visinasred > pozmisa[1] > visinasred - dugmevis: #provera da li je mis u dugmetu
            inbox = True
        else:
            inbox = False
            
    if event.type == pg.MOUSEBUTTONDOWN and inbox == True: #ako je u dugmetu i klikne se, izvrsi se bubble sort
        bubblesort()
while True:
    pg.time.wait(31)
    dugme()


