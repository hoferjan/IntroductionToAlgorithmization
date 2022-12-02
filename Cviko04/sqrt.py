def sqrt(a):
    x = a
    while True:
        newX = 0.5 * (x + a / x)
        if x == newX:
            return newX
        x = newX

print(sqrt(9))