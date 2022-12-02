poly1 = [1, 2, 5]
poly2 = [2, 0, 1, -7]
def polyEval(polynom,x):
    if x==0:
        return polynom[0]
    else:
        sum=0
        for i in range(len(polynom)):
            sum+=(polynom[i])*(x**i)
        return sum

def polySum(poly1,poly2):
    nlst=[]
    if len(poly2)> len(poly1):
        poly1,poly2=poly2,poly1
    counter=0
    for position in range(len(poly2)):
        nlst.append(poly1[position]+poly2[position])
        counter+=1
    for position in range(counter):
        poly1.pop(0)
    if len(poly1) != 0:
        for position in range(len(poly1)):
            nlst.append(poly1[position])
    while nlst[len(nlst)-1] == 0:
        nlst.pop()
    return nlst

def polyMultiply(poly1,poly2):
    lenght1=len(poly1)
    lenght2=len(poly2)
    nlst=[0]*(lenght1+lenght2-1)
    for j in range(len(poly1)):
        for i in range(len(poly2)):
            nlst[j+i] += poly1[j] * poly2[i]

    return nlst


#print(polySum(poly1,poly2))
#print(polyEval(poly1,2))
#print(polyMultiply(poly1,poly2))