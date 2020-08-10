import pygame as pg
import math, random
pg.init()

#promenljive
(sirina, visina) = (1080, 540)
prozor = pg.display.set_mode((sirina,visina))
prozor.fill((255,255,255))

global dugmesir
global dugmevis
(dugmesir, dugmevis) = (150, 75)

(sirinasred, visinasred) = (int(sirina / 2), int(visina / 2))

#dimenzije i podaci za bubble sort dugme
global bubblecenter
global bubblesirina
global bubblevisina
bubblecenter = (142, 104)
bubblesirina = int(sirinasred / 8)
bubblevisina = int(visinasred / 4)

#slova i unos textbox
global font
font = pg.font.Font(None,30)
unostekst = ''

#crtanje
pg.draw.rect(prozor,(50,50,200),(int(bubblesirina), int(bubblevisina), int(dugmesir) , int(dugmevis)))
prozor.blit((font.render(("Broj elemenata:"), True, (0,0,0))),(25,475))
prozor.blit((font.render(("Bubble sort"), True, (255,255,255))),(bubblecenter[0] - dugmesir / 2.5, bubblecenter[1] - dugmevis / 8))

def bubblesort(element):
    #kreiranje liste i random elemenata
    brojelemenata = int(element)
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
    global unostekst
    global tekstrender
    tekstrender = font.render(unostekst, True, (0,0,0))
    prozor.blit(tekstrender,(25,500))
    element = unostekst
    
    event = pg.event.wait()
    if event.type == pg.KEYDOWN:
            unostekst += event.unicode
        
    if event.type == pg.MOUSEMOTION or event.type == pg.MOUSEBUTTONDOWN:
        pozmisa = pg.mouse.get_pos() #kada se klikne ili pomeri mis pronadje se pozicija
        
        print(pozmisa[0],bubblevisina,(bubblecenter[0]+bubblesirina/2),(bubblecenter[0]-bubblesirina))
        if event.type == pg.MOUSEBUTTONDOWN:
            
            if ((pozmisa[0] < bubblecenter[0] + dugmesir / 2) and (pozmisa[0] > bubblecenter[0] - dugmesir / 2)) and ((pozmisa[1] < bubblecenter[1] + dugmevis / 2) and (pozmisa[1] > bubblecenter[1] - dugmevis / 2)):
                bubblesort(element)

while True:
    pg.time.wait(31)
    pg.display.update()
    dugme()


