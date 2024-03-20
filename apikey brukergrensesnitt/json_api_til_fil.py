import Settings
import requests
import json
from bucketlist import Bucket_List

class App():
    def __init__(self) -> None:
        self.favoritter = Bucket_List
       
        
    
    @staticmethod
    def print_valg():
        print("Her kan du hente informasjon")
        print("1 Søk")
        print("2 Hent film info")
        print("3 Legg til favoritter")
        print("4 Vis Favoritter")
        print("5 Slette fra favoritter ")
        print("6 Lagre Favoritter ")
        print("x Avslutt")
        print()

    def kjør(self):
        while True:
            self.print_valg()
            valg = input("Hva vil du gjøre ? ")
            if valg == "1":
                self.søk_film()
            elif valg == "2":
                tittel = input("hvilket film du søker for ")
                self.hent_film_info(tittel)
            elif valg == "3":
                navn  = input("hva vil du at navnet skal bli ? ")
                liste = Bucket_List(navn)
                tittel = input("hva er tittelen til filmen du vil legge til ? ")
                liste.legg_til(tittel)


            elif valg == "4":
                liste.vis()

            elif valg == "5":
                x = 0
                for i in liste:
                    x+= 1
                    print(x, i)
                    valg = input("hvilket vil du slette  ? ")
                    liste.pop(valg-1)

            elif valg == "X":
                print("Avslutter")
                break
            
            else: 
                print("prøv igjen ")

            input("klikk enter for gå til hovedmeny ")


    def hent_film_info(self, tittel):
        """ Hente informasjon om et film"""
        #Konfigurerer kall til API
        api_key = Settings.API_KEY  # Du må erstatte 'din_omdb_api_nøkkel' med din egen 
        url = f'http://www.omdbapi.com/?apikey={api_key}&i={tittel}'  #test her forskjellige kall

        #Kalle tjeneste fra API og hente resultater.
        response = requests.get(url)
        if response.status_code == 200:  # sjekker at HTTP request til API gikk bra.
            film_data = response.json()
            if film_data["Response"] == "False":   #sjekker om OMDb API tjeneste kall gikk bra.
                print(film_data["Error"])
                return None
            return film_data
            

    def lagre_film_info(self, data, filename):
        """ Lagre informasjon om et film"""
        with open(filename, 'w') as json_fil:
            json.dump(data, json_fil, indent=4)


    def lage_bucket_list(self):
        bucket_name = input("hva vil du at navnet skal bli ? ")
        bucket_name = []
        return bucket_name

  



    

if __name__ == '__main__':
    app = App()
    app.kjør()
    film_tittel = input('Skriv inn tittelen på filmen: ')
    film_info = app.hent_film_info(film_tittel)
    if film_info:
        filnavn = f'film_info.json'
        app.lagre_film_info(film_info, filnavn)
        print(f'Filminformasjonen er lagret i "{filnavn}" filen.')
