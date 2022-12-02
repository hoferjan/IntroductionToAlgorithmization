def sum(from_num,to_num):
    sum=0
    for i in range (from_num,to_num+1):
        sum+=i
    return sum

print(sum(5,10))

def sum_while(from_num,to_num):
    cislo=0
    i=from_num
    while i <= to_num:
        cislo += i
        i += 1
    return cislo
print(sum_while(5,10))
