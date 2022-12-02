import math

def leibnizPi(iterations):
    i=1
    counter=0
    pi=0
    while counter != (iterations):
        if (i-1) % 4 == 0 or i ==1:
            pi+=(4/i)
        else:
            pi-=(4/i)
        i += 2
        counter +=1
    return pi

def nilakanthaPi(iterations):
    pi=3 # start from 3 so we will add later
    counter=0
    if iterations == 1:
        return pi
    else:
        repetition=iterations-1 # no need for the first iteration, it is zero
        x=2 #three numbers to multiply and divide by
        y=3
        z=4
        while counter != repetition:
            if x % 4 != 0:
                pi+=4/(x*y*z)
            else:
                pi-=4/(x*y*z)
            x+=2
            y+=2
            z+=2
            counter+=1
    return pi

def newtonPi(init):
    # two values so i can compare them later
    x=init #x0
    y=x-(math.sin(x)/math.cos(x)) #x1
    counter=0
    while x != y:
        if counter % 2 ==0 or counter ==0:
            x=y-(math.sin(y)/math.cos(y))
        else:
            y=x-(math.sin(x)/math.cos(x))
        counter+=1
    return x

print(nilakanthaPi(34))
print(newtonPi(5))

