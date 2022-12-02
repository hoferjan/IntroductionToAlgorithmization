import random

secret=random.randint(1,100)

print(secret)

while True:
    guess = int(input("Guess a number: "))
    if guess<0 or guess >=101:
        print("mimo rozsah")
        break
    else:
        if guess==secret:
            print("YOUVE WON!")
            break
        elif guess<secret:
            print("Too small")
        elif guess>secret:
            print("Too big")