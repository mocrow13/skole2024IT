# fil = open("filhandtering.py", encoding="utf-8")
# data = fil.read()
# print(data)
# fil.close()

# with open("filhandtering.py", encoding = "utf-8") as fil:
#     data = fil.read()
# linjer = data.split("\n")
# print(linjer)

import json 
fil = open("sanger.json", encoding = "utf-8")
sanger = json.load(fil)
print(sanger[0])

with open("sanger.json", encoding = "utf-8") as fil:
    sanger = json.load(fil)
    print(sanger[0])

with open("sanger.json", encoding = "utf-8") as fil:
    poeng = 0 
    sanger = json.load(fil)
    for sang in sanger:
        if sang["artist"] == "Taylor Swift":
            poeng  += 1

print(poeng)


