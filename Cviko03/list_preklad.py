en_to_cz = {"`" : ";", "1" : "+", "2" : "ě", "3" : "š", "4" : "č", "5" : "ř", "6" : "ž", "7" : "ý", "8" : "á", "9" : "í", "0" : "é", "-" : "=", "[" : "ú", "]" : ")", ";" : "ů", "'" : "§", "/" : "-", "!" : "1", "@" : "2", "#" : "3", "$" : "4", "%" : "5", "^" : "6", "&" : "7", "*" : "8", "(" : "9", ")" : "0", "_" : "%", "{" : "/", "}" : "(", ":" : "\"", "\"" : "!", "<" : "?", ">" : ":", "?" : "_"}

text='A tak se stalo, 6e dal39 den vyjelo aut94ko do sv2ta. P5edt9m se samoz5ejm2 rozlou4ilo se sv7mi rodi4i a vzalo si nutn0 v2ci sebou. To bylo ale nad3en9" Tolik jin7ch cest, tolik jin7ch cedul9 a nejen to" Aut94ko pozn8valo i nov0 zem2" Projelo celou Evropu i Asii, dokonce se vydalo i do Ameriky A nejen6e pozn8valo zem2, ale tak0 pr8ci jin7ch aut."'

#print(">" in en_to_cz) #hleda to napravo od dvojtecky

result=""
for char in text:
    if char in en_to_cz:
        result +=en_to_cz[char]
    else:
        result+=char

print(result)

