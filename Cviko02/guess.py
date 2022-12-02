secret = 5
guess=secret-1 #cant be equal and has to start the while loop

if guess == secret:
    print("YOU'VE WON!")
    print("Game over")
while guess != secret:
    guess = int(input("Guess a number: "))
    if secret > guess:
        print("Too small.")
    elif secret < guess:
        print("Too big.")

print("Game over")

