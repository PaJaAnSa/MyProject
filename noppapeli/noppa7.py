# -*- coding: utf-8 -*-
"""
noppa6, joka

* on jaettu moduuleihin
* noppa, joka sisältää funktion main
* noppapeli tuodaan import lauseella 
"""
import os
import noppapeli as np
    
def main() :
    """
    Pääfunktio, jossa 7-nolla pyörii silmukassa kunnes potti on käytetty
    """
    print('7-noppa pelissä käyttäjä asettaa panoksen ja arvaa kahden nopan summan.\n \
    Jos summa on 7 ja käyttäjä on arvannut tasan, hän voittaa panoksensa 10-kertaisena.\n \
    Jos summa ei ole ja käyttäjä on arvannut tasan, hän häviää panoksensa 10-kertaisena.\n \
    Jos summa on alle tai yli ja käyttäjä on arvannut oikein ali tai yli, hän voittaa panoksensa 2-kertaisena.\n \
    Jos summa on alle tai yli ja käyttäjä on arvannut väärin ali tai yli, hän häviää panoksensa.\n\n \
    Pelissä potti on aluksi 100 ja loppuu, kun koko potti on käytetty.\n\n')
    if os.path.exists('potti.dat') :
        with open('potti.dat') as f :
            np.potti = int(f.read())
            if np.potti <= 0 :
                print('Hävisit koko potin edellisessä pelissä. Peli alkaa alusta')
                np.potti = 100
            print(f'potti on {np.potti}')
    
    while True :
        panos = np.lue_panos()
        arvaus = np.lue_arvaus()
        summa, nopat = np.heita()
        #pelin historia potti, panos, arvaus, nopat, uusi potti
        with open('peli.log', 'a+') as f :
            f.write(f'{np.potti}, ')
            potti = np.tarkista(panos, arvaus, summa)
            f.writelines(f'{panos}, {arvaus}, {nopat[0]}, {nopat[1]}, {potti}\n')
        #potti talteen
        with open('potti.dat', 'w+') as f :
            f.write(str(potti))
        if potti <=  0 : 
            break           
        if input('Uusi heitto [E]? ').lower() == 'e' :
            break
        pass
    print('Kiitos hyvästä pelistä.')        


# main- funktio ei ole Pythonissa erityisasemassa, mutta 
# alla oleva rivi on yleinen sovittu tapa tarkistaa suoritetaanko scripti suoraan vai
# tuodaanko se moduulina toiseen moduuliin, jolloin main ei suoriteta

if  __name__ == '__main__' :
    main()