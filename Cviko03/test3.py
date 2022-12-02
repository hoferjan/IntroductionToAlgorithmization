def rozmnoz_text(text:str, kolikrat:int)->str:
  vysledek:int = text * kolikrat
  return vysledek
a:bool = "Pingu"
b:str = 5
c:float = rozmnoz_text(b, a)
print(c)