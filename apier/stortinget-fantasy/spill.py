import os 
import platform 
import json,sys
from politiker import Politiker
from fantasiparti import Fantasiparti
def rens_terminal (): 
    if platform.system == "Windows" or sys.platform == "win32": 
        os.system( "cls" ) 
    else: 
        os.system( "clear" )
    
with open ( "politikere.json" , "r" , encoding = "utf-8" ) as fil: 
    data = json.load(fil) 
politikere_data = data [ "dagensrepresentanter_liste" ] 
politikere = [] 
for politiker_ordbok in politikere_data : 
    ny_politiker = Politiker(politiker_ordbok) 
    politikere.append(ny_politiker) 

rens_terminal()
print("Stortinget Fantasy ")
print("Du må stifte et parti for å spille spillet ")
print("Du må ha et navn for partiet ditt ")
partinavn =  input("navnet ? ")
print("hva heter du ")
partieier = input("")
print(f"gratulerer {partinavn} ble opprettet av {partieier} ")
spillerparti = Fantasiparti(partinavn, partieier)
print("trykk enter for å starte spillet")
input()





while True :
    rens_terminal () 
    print ( " -- Stortinget-fantasy --" )
    print(f"Parti : {spillerparti.navn}")
    print(f"Saldo : {spillerparti.saldo}")
    print(f"Saldo : {len(spillerparti.politikere)}")
    print ( "1: Vis politikeroversikt" ) 
    print ( "2: Mitt parti" ) 
    print ( "3: Kjøp politiker" )
    print ( "4: Selg politiker" )
    print ( "5: Avslutt" ) 
    brukervalg = input ( "> " ) 
    if brukervalg == "1" :
        print ( "politikeroversikt" ) 
        for politiker in politikere :
            print (politiker, politiker.id) 
            print ( "Trykk enter for å gå tilbake til hovedmenyen" ) 
        input () 
    elif brukervalg == "2" : 
        rens_terminal () 
        spillerparti.vis_partioversikt(Politiker)
        print ( "Trykk enter for å gå tilbake til hovedmenyen" ) 
        input () 
    elif brukervalg == "3" : 
        rens_terminal () 
        print ( "Kjøp politiker" ) 
        print ()
        print ( "Hvem ønsker du å kjøpe? Skriv ID til politiker." )
        for politiker in politikere:
            print(politiker, politiker.id)
        politiker_id = input ( "> " )
        for politiker in politikere :
            if politiker.id == politiker_id and politiker not in spillerparti.politikere :
                spillerparti.kjøp_politiker(politiker) 
                break 
        print ( "Trykk enter for å gå tilbake til hovedmenyen" ) 
        input () 
    elif brukervalg == "4" : 
        rens_terminal () 
        print ( "Selg politiker" ) 
        print ()
        print ( "Hvem ønsker du å selge? Skriv ID til politiker." )
        for politiker in spillerparti.politikere:
            print(politiker, politiker.id)
        politiker_id = input ( "> " )
        
        for spillerparti_id in spillerparti.politikere :
            if politiker.id == politiker_id :
                spillerparti.selg_politiker(politiker) 
                break 
        print ( "Trykk enter for å gå tilbake til hovedmenyen" ) 
        input () 
    
    
    elif brukervalg == "9" : 
        print ( "avslutter.." ) 
        break 
    else : 
        print ( "Trykk enter for å gå tilbake til hovedmenyen" ) 
        input ()
        print ( "Takk for nå" )