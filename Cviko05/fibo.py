def fibo(n):
    list =[0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            x=list[-2]+list[-1]
            list.append(x)
    return list

print(fibo(8))