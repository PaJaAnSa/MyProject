# -*- coding: utf-8 -*-
"""
noppapeli, joka sisältää funktiot käyttäjän valinnan lukemiseen, 
  noppien heittämiseen ja tuloksen ilmoittamiseen sekä potin suuruuden tarkistamiseen.
* kysyy käyttäjältä arvauksen kahden nopan silmälukujen summasta (yli, tasan tai alle 7)
* pitää kirjaa potista. Ohjelman aluksi potti on 100 ja jokaisen heiton 
  jälkeen voitettu panos lisätään pottiin ja hävitty panos vähennetään potista. 
  Peliä voi pelata niin kauan kuin potti on suurempi kuin 0. Pelaaja ei voi jäädä pankille velkaa.
* kysyy käyttäjältä panoksen, joka voi olla välillä 1 - potti
* heittää (arpoo satunnaisen luvun välillä [1, 6]) kaksi noppaa ja 
  asettaa molempien silmäluvut yhteen muuttujaan (muuttuja sisältää 2 kpl erillisiä lukuja)
* näyttää noppien silmäluvut, niiden summan ja käyttäjän arvauksen
* näyttää arvasiko käyttäjä
* * täsmälleen oikein (tasan 7), jolloin käyttäjä voittaa panoksensa kymmenkertaisena
* * täsmälleen väärin (arvaus tasan ja lukema ei ole 7), jolloin käyttäjä 
    häviää panoksensa kymmenkertaisena. 
* * ali tai yli arvaus oikein, jolloin käyttäjä tuplaa panoksensa
* * ali tai yli arvaus väärin, jolloin käyttäjä menettää panoksensa
"""

import random

potti = 100 #globaali (moduulin sisällä) muuttuja
# globaalin muuttujanarvon voi funktioissa lukea
# kirjoittaminen (=muuttaminen) vaatii funktiossa global avainsanan käyttöä

def lue_arvaus() :
    """
    kysyy käyttäjältä arvauksen kahden nopan silmälukujen summasta 
    (yli, tasan tai alle 7)
    """
    arvaukset = {'y', 'a', 't'}
    while True : 
        arvaus = input("Arvaa onko noppien summa yli, ali vai tasan 7 [y, a, t]: ")#tarkistaaa arvauksesta vain 1. merkin arvaus[0]
        if arvaus[0].lower() in arvaukset :
            arvaus = arvaus[0].lower()
            break
        else :
            print("Tarkista arvauksesi") 
    return arvaus

def laske_potti(panos = 0) :
    """ 
    pitää kirjaa potista. Ohjelman aluksi potti on 100 ja jokaisen heiton 
    jälkeen voitettu panos lisätään pottiin ja hävitty panos vähennetään potista. 
    Peliä voi pelata niin kauan kuin potti on suurempi kuin 0. Pelaaja ei voi jäädä pankille velkaa.
    """  
    global potti # muutetaan globaalin muuttujan arvoa
    potti =  potti + panos if panos > 0 or (panos < 0 and  panos <= potti)  else 0   

def lue_panos() :
    """
    kysyy käyttäjältä panoksen, joka voi olla välillä 1 - potti
    """  
    while True :
        try :
            panos = int(input(f"Aseta panoksesi[1, {potti}]: "))
            if panos >= 1 and panos <= potti :
                laske_potti(panos) #koko potti ennen heittoa
                print(f'Potti on {potti}')            
                break
            else :
                print("Tarkista panoksesi")
        except ValueError :
            print(f'vain kokonaislukuja [1, {potti}]')
    return panos

def heita() :
    """
    heittää (arpoo satunnaisen luvun välillä [1, 6]) kaksi noppaa ja 
    asettaa molempien silmäluvut yhteen muuttujaan (muuttuja sisältää 2 kpl erillisiä lukuja)
    """    
    nopat = [random.randint(1,6), random.randint(1,6)]
    summa = sum(nopat)  #Pythonin valmis funktio
    print(f"noppien summa on {summa} ({nopat[0]} + {nopat[1]})") 
    return summa, nopat

def tarkista(panos, arvaus, summa) :
    """
    näyttää noppien silmäluvut, niiden summan ja käyttäjän arvauksen
    * näyttää arvasiko käyttäjä
    * * täsmälleen oikein (tasan 7), jolloin käyttäjä voittaa panoksensa kymmenkertaisena
    * * täsmälleen väärin (arvaus tasan ja lukema ei ole 7), jolloin käyttäjä 
        häviää panoksensa kymmenkertaisena. 
        * * ali tai yli arvaus oikein, jolloin käyttäjä tuplaa panoksensa
        * * ali tai yli arvaus väärin, jolloin käyttäjä menettää panoksensa
    """
    tilanne = str()
    if arvaus == 't'and summa == 7 : 
        panos *= 10
        tilanne = f'Voitit panoksesi kymmenkertaisena - {panos} pottiin!'
    elif (arvaus == 'a' and summa < 7) or (arvaus == 'y' and summa > 7) :
        panos *= 2
        tilanne = f'Voitit panoksesi kaksinkertaisena - {panos} pottiin!'
    elif arvaus == 't'and summa != 7 : 
        panos *= 10
        tilanne = f'Hävisit panoksesi kymmenkertaisesti - {panos} potista pois!'
        panos *= -1
    elif (arvaus == 'a' and summa >= 7) or (arvaus == 'y' and summa <= 7) :
        tilanne = f'Hävisit panoksesi - {panos} potista pois!'
        panos *= -1
    else :
        print("Noppien heitto ei tällä hetkellä onnistu, koita uudelleen myöhemmin.")
    laske_potti(panos)
    print(f'{tilanne}\nPotti on {potti if potti >= 0 else " käytetty"}')
    return potti