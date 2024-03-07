import requests
 
respons = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=2")
data = respons.json()
data
# hånd = data["cards"]
# for kort in hånd:
#     print(kort["value"], kort["suit"])

import requests
import json
# dumper dataen i en json-fil
respons = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=60.10&lon=10" , headers={ 'User-Agent': 'Python'})
data = respons.json()
with open("met.json", "w", encoding="utf-8") as fil:
    json.dump(data, fil, indent=2, ensure_ascii=False)
værtype = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
temperatur = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
print(f"I Sandvika er det {temperatur} grader og {værtype}")


