sum=0
amount=0

while True:
    grade = int(input("Gimme a grade"))
    if grade==0:
        break
    amount+=1
    sum+=grade


aver=sum/amount

print(aver)