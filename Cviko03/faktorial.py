def fact(num):
    result=1
    for i in range(num, 1,-1):
        print(">>>",i)
        result *= i
    return result


print(fact(5))