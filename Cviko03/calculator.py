def addition(x, y):
    return x+y

def subtraction (x , y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y==0:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return float(x/y)

def modulo(x,y):
    x=float(x)
    y=float(y)
    if (x >= y) & (y > 0):
        return x%y
    else:
        raise ValueError('This operation is not supported for given input parameters')

def secondPower(x):
    return x**2

def power(x,y):
    if y >= 0:
        return float(x**y)
    else:
        raise ValueError('This operation is not supported for given input parameters')

def secondRadix(x):
    if x>0: return x**(1/2)
    else: raise ValueError('This operation is not supported for given input parameters')

def magic(x,y,z,k):
    if y+z == 0:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        n=(((x + k)/(y + z)) + 1)
        return n

def control(a,x,y,z,k):
    if a=="ADDITION":
        return addition(x,y)
    elif a=="SUBTRACTION":
        return subtraction(x,y)
    elif a=="MULTIPLICATION":
        return multiplication(x,y)
    elif a=="DIVISION":
        return division(x,y)
    elif a=="MOD":
        return modulo(x,y)
    elif a=="POWER":
        return power(x,y)
    elif a=="SECONDRADIX":
        return secondRadix(x)
    elif a=="MAGIC":
        return float(magic(x,y,z,k))
    else:
        raise ValueError('This operation is not supported for given input parameters')

    '''
    functions={
    "ADDITION" : addition(x,y),
    "SUBTRACTION" : subtraction(x,y),
    "MULTIPLICATION" : multiplication(x,y),
    "DIVISION" : division(x,y),
    "MOD" : modulo(x,y),
    "POWER" : power(x,y),
    "SECONDRADIX" : secondRadix(x),
    "MAGIC" : magic(x,y,z,k)
    }
    return functions[a]
    '''

#print(control("MAGIC",4,0,0,4))