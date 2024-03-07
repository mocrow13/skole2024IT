## Penger tjent per sang

Hent inn land fra bruker {input}



### Pseudokode i "naturlig språk"

"""pseudokode

Hvis land =  norge: 
    print 0.44# per sang
Ellers Hvis land = sverige:
    print 0.34$ per sang

Ellers
    print 0.22 per sang

"""

### Pseudokode som følger UDIRs standard

"""pseudo
SET land to READ "Hvilket land er du fra "
If land EQUAL TO Norge
    THEN DISPLAY "$0.44 per sang"

ELSE IF land EQUAL TO Sverige
    THEN DISPLAY "0.34 per sang"

ELSE 
    THEN DISPLAY "0.22 per sang"

ENDIF
"""

### Python Kode  

'''python

def finnutlandet(land):
    land = input("hvilket land kommer du fra")
    if land == "norge":
        print("0.44$ per sang")

    elif land == "sverige":
        print("0.34 dollar per sang")

    else:
        print("0.22 dollar per sang ")
'''

## Andell penger per sang 

### pseudekode i naturlig språk 

Hent inn antall streams fra bruker (input)

hvis antall streams er større enn 30 millioner 
    print penger tjent per sang lik 70% 

Ellers hvis antall streams er større enn 1.4 millioner
    print penger tjent per sang lik 40%

Ellers 
    print penger tjent per sang lik 0%

### pseudekode som følger UDIRs standard

SET streams TO READ "hvor mange streams har brukeren"
    IF streams GREATER THEN 3000000
        THEN DISPLAY "PENGER TJENT PER SANG LIK 70%
    ELSE IF streams LESSER THAN 3000000 AND STREAMS GREATER THEN 1400000
    
        THEN DISPLAY "PENGER TJENT PER SANG LIK %40

    ELSE
        THEN DISPLAY "PENGER TJENT PER SANG LIK %0