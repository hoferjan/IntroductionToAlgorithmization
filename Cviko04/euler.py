def fact(num):
    result=1
    for i in range(num, 1,-1):
        result *= i
    return result

def euler(iter_count):
    suma=0
    for i in range (iter_count+1):
        suma+=1/(fact(i))
    return suma

print(euler(99999))