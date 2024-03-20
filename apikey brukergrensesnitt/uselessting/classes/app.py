import requests as req

class App():
    def __init__(self, apikey) -> None:
        self.apikey = apikey

    def hent_data():
        
        url = "http://numbersapi.com/100/"

        resultat = req.get(url)

        print(f"Statuskode: {resultat.status_code}")