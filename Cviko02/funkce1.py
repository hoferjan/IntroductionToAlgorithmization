import math

def obsah_kruhu(polomer): #davat si pozor na popis promennych
    o = math.pi* math.pow(polomer,2) #v ramci fce mam lokalni promenne
    return o

print(obsah_kruhu(4))
