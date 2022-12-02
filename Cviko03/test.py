def division(x,y):
    if y==0:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return x/y

print(division(1,0))

