def is_prime(x:int) ->bool:
    for i in range (2,x):
        if x%i ==0:
            return False
    return True

print(is_prime(8))