import random

def generate_random_list(count):
    result = []
    for i in range(count):
        result.append(random.randint(1,1000))
    return result
def max_value(array):
    max=0
    for number in array:
        if number> max:
            max=number
    return max

def average(array):
    lenght=len(array)
    sum=0
    for number in array:
        sum+=number
    return (sum/lenght)


rnd_num=(generate_random_list(10))
print(rnd_num)
print(max(rnd_num))
print(average(rnd_num))
print(median(rnd_num))