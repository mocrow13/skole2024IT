#https://github.com/thorcc/IT2-VGS-2324/blob/master/databehandling-og-algoritmer/algoritmer.md#eksempel-2-spotify
# # Sandvikas Spotify bibliotek
# # Versjon: 0.0.1
# # Forfatter: thorcc
# import requests
# import json 

# """
# Eksempel på bruk:
# from spotify import weekly_top_songs_global

# sanger = weekly_top_songs_global() 
# """

# def weekly_top_songs_global():
#     """Henter sangene i spillelisten "Weekly Top Songs: Global

#     Returnerer
#     ----------
#     list<dict>
#         En liste med ordbøker, der hver ordbok er en sang
#         Eks på sang:
#             {
#                 "navn": "Dead of Night", 
#                 "artist": "Orville Peck", 
#                 "bilde_url": "https://i.scdn.co/image/ab6761610000e5eb7b1eab5bbcfd5b2dd57c1753"
#             }
#     """


#     spotify_url = "https://charts-spotify-com-service.spotify.com/public/v0/charts"
#     respons = requests.get(spotify_url) # gjør en spørring til spotify_url (henter innholdet på nettadressen)
#     data = json.loads(respons.content) # gjør innholdet om til en ordbok
    
#     sanger = [] # En tom liste som skal fylles med sanger
#     toppliste = data["chartEntryViewResponses"][0] # Henter ut den første listen, som er "Weekly Top Songs: Global"
#     sangliste = toppliste["entries"]  # Henter listen med sanger
#     for sang in sangliste: # Går gjennom hver sang i listen sangliste:
#         # oppretter en ny ordbok for hver sang
#         ny_sang = {
#             "navn": sang["trackMetadata"]["trackName"],
#             "artist": sang["trackMetadata"]["artists"][0]["name"],
#             "bilde_url": sang["trackMetadata"]["displayImageUri"],
#         }
#         sanger.append(ny_sang) # legger ordboken ny_sang i listen sanger
#     return sanger # returnerer listen sanger

# sanger = weekly_top_songs_global

# fil = open("sanger.json", "w")
# json.dump(sanger, fil, indent = 2)
# fil.close()


# with open("sanger.json", encoding = "utf-8") as fil:
#     poeng = 0 
#     sanger = json.load(fil)
#     for sang in sanger:
#         if sang["artist"] == "Taylor Swift":
#             poeng  += 1

# print(poeng)

# artister = {
# }
# for sang in sanger:
#     if sang["artist"] in artister:
        
#         artister[sang["artist "]] += 1
#     else: 
#         artister[sang["artist "]] = 1
# print(artister)


# artist_liste = list(artister)

# hoyeste_artist = ""
# hoyeste_antall = -1




# for  artist  in artister:
#     print(artist)
#     antall_sanger = artister(artist)
#     print(antall_sanger)
#     if antall_sanger > hoyeste_antall:
#         hoyeste_artist = artist
#         hoyeste_antall = antall_sanger

# print(hoyeste_artist, hoyeste_antall)



import requests
import json

def weekly_top_songs_global():
    spotify_url = "https://charts-spotify-com-service.spotify.com/public/v0/charts"
    respons = requests.get(spotify_url)
    data = json.loads(respons.content)
    
    sanger = []
    toppliste = data["chartEntryViewResponses"][0]
    sangliste = toppliste["entries"]
    
    for sang in sangliste:
        ny_sang = {
            "navn": sang["trackMetadata"]["trackName"],
            "artist": sang["trackMetadata"]["artists"][0]["name"],
            "bilde_url": sang["trackMetadata"]["displayImageUri"],
        }
        sanger.append(ny_sang)
    
    return sanger

# Kall funksjonen for å få listen over sanger
sanger = weekly_top_songs_global()

# Lagre sanger i en JSON-fil
with open("sanger.json", "w", encoding="utf-8") as fil:
    json.dump(sanger, fil, indent=2)

# Åpne JSON-filen og les innholdet
with open("sanger.json", encoding="utf-8") as fil:
    sanger = json.load(fil)

# Sjekk antall sanger av artisten "Taylor Swift"
poeng = sum(1 for sang in sanger if sang["artist"] == "Taylor Swift")
print(f"Antall sanger av Taylor Swift: {poeng}")

# Lag en dictionary for å telle antall sanger per artist
artister = {}
for sang in sanger:
    artist = sang["artist"]
    if artist in artister:
        artister[artist] += 1
    else:
        artister[artist] = 1

print("Antall sanger per artist:")
# print(artister)

# Finn artisten med flest sanger
# hoyeste_artist = max(artister, key=artister.get)
# hoyeste_antall = artister[hoyeste_artist]

# print(f"{hoyeste_artist} har flest sanger med {hoyeste_antall} sanger.")

hoyeste_artist = ""
hoyeste_antall = -1


import json

# Åpne JSON-filen og les innholdet
with open("sanger.json", encoding="utf-8") as fil:
    sanger = json.load(fil)

hoyeste_artist = ""
hoyeste_antall = -1

artister = {}

for sang in sanger:
    artist = sang["artist"]
    
    if artist in artister:
        artister[artist] += 1
    else:
        artister[artist] = 1

for artist, antall_sanger in artister.items():
    # print(f"{artist}: {antall_sanger} sanger")
    if antall_sanger > hoyeste_antall:
        hoyeste_artist = artist
        hoyeste_antall = antall_sanger

print(f"{hoyeste_artist} har flest sanger med {hoyeste_antall} sanger.")


