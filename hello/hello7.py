'''
Hello7 on ohjelma, joka täydentää hello6-ohjelmaan valikon, josta käyttäjä voi valita:
tuo tiedot, joka hakee aikaisemmin annetut tiedot tiedostosta (htiedot.csv) ja tulostaa ne näytölle
syötä uusi, joka toimii kuten tehtävän 5a ohjelma, mutta tulosta-funktio myös tallentaa tiedot tiedoston htiedot.csv loppuun
näytä tiedot, joka näyttää kaikki tiedot (kaikki ohjelmassa syötetyt ja tiedostosta haetut tiedot) joko korttimuodossa tai riveillä
tallenna kortit, joka tallentaa kortit htiedot.txt tiedostoon kortti-muotoilussa 
'''
import os
from datetime import date
import kortti as k

def menu():
    '''
    Ohjelmassa on valikko, josta käyttäjä voi valita:
        - tuo tiedot, joka hakee aikaisemmin annetut tiedot tiedostosta (htiedot.csv) ja tulostaa ne näytölle
        - syötä uusi, joka toimii kuten tehtävän 5a ohjelma, mutta tulosta-funktio myös tallentaa tiedot tiedoston htiedot.csv loppuun
        - näytä tiedot, joka näyttää kaikki tiedot (kaikki ohjelmassa syötetyt ja tiedostosta haetut tiedot) joko korttimuodossa tai riveillä
        - tallenna kortit, joka tallentaa kortit htiedot.txt tiedostoon kortti-muotoilussa 
    '''
    print('1. Tuo tiedot tiedostosta\n2. Syötä uusi\n3. Näytä kaikki\n4. Tallenna\n5. Lopeta')
    while True :
        try :
            a = int(input(': '))
            if a > 0 and a <= 5 :
                break
            else :
                print('valitse 1-5')
                continue
        except :
            print('valitse 1-5')
            continue
    return a
        
        
 
def main() :
    """
    Pääfunktio, jossa hello pyörii silmukassa kunnes käyttäjä ei enää halua 
    antaa lisää tietoja
    """
    
    henkilot = dict() #kerätään henkilöt dictionaryyn
    id = 0 #juokseva numero, jokaiselle henkilölle oma id (=avain)
    tiedosto = 'htiedot.csv'
    korttitiedosto = 'htiedot.txt'

    while True: 
        a = menu()
        if a == 1: #Tuo csv-tiedostosta tiedot
            f1 =  None
            try :
                f1 =  open(tiedosto, 'r')
                for line in f1 :
                    b = line.strip().split(',')
                    if(len(b) == 2) : #nimi, spvm
                        b[1] = k.tarkistaspvm(b[1])
                        #lisää dictionaryyn luetun ruvin key-avaimen valueksi
                        henkilot[id] = b
                        id += 1
                f1.close()
            except (FileNotFoundError, IOError) as error :
                print(f'tapahtui virhe: {error}')
            else :
                print(f'{id} henkilön tiedot luettu')
            finally :
                if f1 != None :
                    f1.close()               

        elif a == 2: # Syötä uusi ja tallenna se csv-tiedoston loppuun
            henkilot[id] = k.kysytiedot()
            k.tulosta(henkilot[id])
            f = None
            try :                
                f = open(tiedosto, 'a+') #avaa kirjoitettavaksi loppuun 
                #kirjoittaa nimen, päivämäärän muutettuna merkkijonoksi ja rivinvaihdon
                f.writelines(henkilot[id][0] + ',' + date.strftime(henkilot[id][1], '%d.%m.%Y' + '\n')) 
            except IOError as error :
                print(f'tapahtui virhe: {error}')
            finally :
                if f != None :
                    f.close()
            id += 1  

        elif a == 3: # Näytä kaikki
           for key in henkilot :
                k.tulosta(henkilot[key])

        elif a == 4 : #Tallenna kortti-muodossa
            #poistaa edellisen tiedoston 
            if os.path.exists(korttitiedosto) :
                os.remove(korttitiedosto)
            for key in henkilot :
                k.tulostatiedostoon(henkilot[key], korttitiedosto)

        else: # Lopeta
            break
        


# main- funktio ei ole Pythonissa erityisasemassa, mutta 
# alla oleva rivi on yleinen sovittu tapa tarkistaa suoritetaanko scripti suoraan vai
# tuodaanko se moduulina toiseen moduuliin, jolloin main ei suoriteta

if  __name__ == '__main__' :
    main()
    









