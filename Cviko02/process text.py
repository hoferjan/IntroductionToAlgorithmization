def vyhod_aoe(text):
    vysledek=""
    for znak in text:
        if znak != "a" and znak != 'o' and znak != 'e':
            vysledek += znak
    return vysledek


with open("potter.txt", "r") as potter, open("pttr.txt", "w") as vystup:
    for radek in potter:
        vystup.write(vyhod_aoe(radek))