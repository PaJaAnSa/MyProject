# -*- coding: utf-8 -*-
"""
kortti moduuli on jaettu funktioihin:
* kysytiedot, joka kysyy käyttäjän nimen ja syntymäajan (päivä, kuukausi, vuosi) ja
  tarkistaa, että syöte on järkevä (todellinen päivämäärä) myös jos vuosi on 
  karkausvuosi ja päivä 29. helmikuuta. Jos käyttäjän syöte on väärä, ohjelma 
  ilmoittaa sen käyttäjälle ja pyytää uuden syntymäajan kunnes syöte on kelvollinen. 
  Funktio palauttaa nimen ja syntymäajan kutsujalle (main-funktio), 
  josta ne luetaan yhteen muuttujaan htiedot 
* laskeika, jolla on parametri spvm, joka on käyttäjän antama päivämäärä, ja 
  joka tarkistaa onko spvm:n päivä jo mennyt, jolloin ikä on kuluva vuosi - syntymävuosi, 
  muutoin ikä on kuluva vuosi - syntymävuosi - 1. Funktio palauttaa iän.
* tulosta, jolla on parametri htiedot, ja joka tulostaa tehtävän tekijän nimen, 
  syntymäajan ja iän kaikki eri riveille vakiokokoiseen  50 tai 51 merkin levyiseen
  "korttiin" ympäröitynä tähdillä. Nimi, syntymäaika ja ikä ovat kortin keskellä niin,
  että parillisen mittainen nimi on 50 ja parittoman mittainen 51 merkin levyisen kortin keskellä. 
  Jos nimen pituus on yli 46 merkkiä nimi jaetaan kahdelle riville. esim.
    **********************************************

    *                                                             *

                          Tiina Ferm

                            16.10.64

                                55

    *                                                             *

    **********************************************
        tulosta, jolla on parametri htiedot (nimi, spvm), ja joka tulostaa tehtävän tekijän nimen, 
    syntymäajan ja iän kaikki eri riveille vakiokokoiseen  50 tai 51 merkin levyiseen
    "korttiin" ympäröitynä tähdillä. Nimi, syntymäaika ja ikä ovat kortin keskellä niin,
    että parillisen mittainen nimi on 50 ja parittoman mittainen 51 merkin levyisen
    kortin keskellä. 
    Jos nimen pituus on yli 46 merkkiä nimi jaetaan kahdelle riville. 

"""


from datetime import date


def tarkistaspvm(pm):
    '''
    Tarkistaa merkijonon kelvollisuuden päivämääräksi, joka on ennen kuluvaa päivää.
    Palauttaa päivämäärän tai nostaa ValueError
    '''
    spvm = pm.split('.')   
    if len(spvm) == 3 :        
        #annetaan luetuille tiedoille lyhyemmät nimet, ei tarvitse testata onko 
        #käyttäjä osannut antaa tarpeellisen määrän tietoa
        #jos käyttäjä ei ole antanut numeroita, napataan ValueError
        pv = int(spvm[0])
        kk = int(spvm[1])
        vvvv = int(spvm[2])                
        if (pv > 0 and kk > 0 and vvvv > 0) and \
            (kk == 2 and  not (vvvv % 4 == 0 and vvvv % 400 == 0)  and pv <= 28) \
            or (kk == 2  and  vvvv % 4 == 0 or (vvvv % 100 == 0 and vvvv % 400 == 0) and pv <= 29) \
            or ((kk == 4 or kk == 6 or kk == 9 or kk == 11 ) and pv <= 30)\
            or ((kk == 1 or kk == 3 or kk == 5 or kk == 7 or kk == 10 or kk == 12) \
                and pv <= 31):                          
            #muodosta päivämäärä date(vuosi, kuukausi, päivä)
            spvm = date(vvvv,  kk, pv)            
            #tarkista syöte (ennen tätä päivää, tänään syntynyt käy)
            nyt = date.today()
            if  spvm > nyt :
                raise ValueError('päivämäärää ei ole vielä ollut')  
        else :
            raise ValueError('päivämäärä ei ole kelvollinen')
    else :
        raise ValueError('syntymäajasta puuttuu tietoa')
    return spvm

def kysytiedot() :
    ''' 
    kysyy käyttäjän nimen ja syntymäajan (päivä, kuukausi, vuosi) ja
    tarkistaa, että syöte on järkevä (todellinen päivämäärä) myös jos vuosi on 
    karkausvuosi ja päivä 29. helmikuuta. Jos käyttäjän syöte on väärä, ohjelma 
    ilmoittaa sen käyttäjälle ja pyytää uuden syntymäajan kunnes syöte on kelvollinen. 
    Funktio palauttaa nimen ja syntymäajan kutsujalle 
    '''
    while True :    
        try :
            nimi = input('Nimi? ') #vaihdetaan teksti paremmin sopivaksi 
            #kysytään joko päivä, kuukausi ja vuosi erikseen tai kaikki yhdessä
            #ja jaetaan listaan . kohdalta
            spvm = tarkistaspvm(input('Syntymäaika [pp.kk.vvvv]? '))  
            break
        except ValueError :
            print('Tarkista päivämäärä') 
            continue
    return nimi, spvm #palauttaa yksittäiset tiedot yhteen muttujaan
  
def laskeika(spvm) :
    '''
    laskeika, jolla on parametri spvm, joka on käyttäjän antama päivämäärä, ja 
    joka tarkistaa onko spvm:n päivä jo mennyt, jolloin ikä on kuluva vuosi - syntymävuosi, 
    muutoin ikä on kuluva vuosi - syntymävuosi - 1. Funktio palauttaa iän.
    '''
    nyt = date.today()
    if spvm <= nyt :
        #syntynyt ennen tätä päivää
        if nyt.month < spvm.month or nyt.month == spvm.month and nyt.day < spvm.day :
            #syntymäpäivä on vasta tulossa
            ika = nyt.year - spvm.year -1
        else :
            ika = nyt.year - spvm.year                                               
    return ika
    
def tulosta(htiedot) :
    #nimen pituus yli 46 merkkiä, oletus ettei yli 2x46
    #ja jaettavissa jotenkin järkevästi tyhjästä välistä

    loput = 0
    nimi = htiedot[0] #lyhyempi nimi
    if len(nimi) > 46 :
        nimet = nimi.split(' ')
        #tyhjä väli jakaa nimen
        if len(nimi) >= 2 :
            nimi = nimet[0]
            loput = ' '.join(nimet[1:])
        else : #yksi pitkä merkkijono
            loput = nimi[46:] #slice operaatio 46 merkistä loppuun
            nimi = nimi[0:46] #nimi muuttujan sisältö muuttuu                
    #kortin leveys pariton nimen pituus
    if len(nimi) % 2 != 0 :
        leveys = 51
    else : #parillinen
        leveys = 50                     
    #tulostuksen muotoilu
    #käyttää htiedot kokoelmaa tulostuksessa
    a = '*' * leveys
    b = '*' +  ' ' * (leveys - 2) + '*'
    c = ' ' * (leveys//2 - (len(nimi)//2))
    if loput != 0 :
        d = ' ' * (leveys//2 - (len(loput)//2))
    e = ' ' * (leveys//2 - (len(str(htiedot[1]))//2))
    f = ' ' * (leveys//2 - 1)    
    print(a)
    print(b)        
    print(c, nimi)
    if loput != 0 :
        print(d, loput)  
    print(e, htiedot[1]) 
    print(f, laskeika(htiedot[1]))
    print(b)
    print(a)
    
def tulostatiedostoon(htiedot, tiedosto) :
    #nimen pituus yli 46 merkkiä, oletus ettei yli 2x46
    #ja jaettavissa jotenkin järkevästi tyhjästä välistä

    loput = 0
    nimi = htiedot[0] #lyhyempi nimi
    if len(nimi) > 46 :
        nimet = nimi.split(' ')
        #tyhjä väli jakaa nimen
        if len(nimi) >= 2 :
            nimi = nimet[0]
            loput = ' '.join(nimet[1:])
        else : #yksi pitkä merkkijono
            loput = nimi[46:] #slice operaatio 46 merkistä loppuun
            nimi = nimi[0:46] #nimi muuttujan sisältö muuttuu                
    #kortin leveys pariton nimen pituus
    if len(nimi) % 2 != 0 :
        leveys = 51
    else : #parillinen
        leveys = 50                     
    #tulostuksen muotoilu
    #käyttää htiedot kokoelmaa tulostuksessa
    a = '*' * leveys
    b = '*' +  ' ' * (leveys - 2) + '*'
    c = ' ' * (leveys//2 - (len(nimi)//2))
    if loput != 0 :
        d = ' ' * (leveys//2 - (len(loput)//2))
    e = ' ' * (leveys//2 - (len(str(htiedot[1]))//2))
    f = ' ' * (leveys//2 - 1) 
    f1 = None
    try :
        f1 = open(tiedosto, 'a+')
        f1.write(a + '\n')
        f1.write(b + '\n')        
        f1.write(c + nimi + '\n')
        if loput != 0 :
            f1.write(d + loput + '\n')  
        f1.write(e + date.strftime(htiedot[1], '%d.%m.%Y') + '\n')
        f1.write(f + str(laskeika(htiedot[1])) + '\n')
        f1.write(b + '\n')
        f1.write(a + '\n')    
    finally :
        if f1 != None :
            f1.close()


