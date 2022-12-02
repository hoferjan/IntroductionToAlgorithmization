poly=[1,4,3]
cars=["Audi","Tesla", "BMW"]

def sortNumbers(poly,deter):
    reverse=[]
    for j in range(len(poly)):
        for i in range(len(poly)-1-j):
            if poly[i] > poly[i+1]:
                poly[i], poly[i+1] = poly[i+1], poly[i]
                if deter == "ASC":
                    return poly
                elif deter == "DESC":
                    for item in poly:
                        reverse.insert(0,item)
                    return reverse



def sortData(rep,cars,deter):
    if len(rep) != len(cars):
        raise ValueError('Invalid input data')
    else:
        for j in range(len(rep)):
            for j in range(len(rep)):
                for i in range(len(rep) - 1 - j):
                    if deter == "ASC":
                        if rep[i] > rep[i + 1]:
                                rep[i], rep[i + 1] = rep[i + 1], rep[i]
                                cars[i], cars[i + 1] = cars[i + 1], cars[i]
                    elif deter == "DESC":
                        if rep[i] < rep[i + 1]:
                            rep[i], rep[i + 1] = rep[i + 1], rep[i]
                            cars[i], cars[i + 1] = cars[i + 1], cars[i]
    return cars

#print(sortData(poly,cars,"DESC"))
print(sortNumbers(poly,"DESC"))