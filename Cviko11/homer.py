"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    if len(fridge) == 0:
        return -1
    maxExp = 0
    for food in fridge:
        if food.expiration > maxExp:
            maxExp = food.expiration
    return maxExp


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    histogram = []
    places = maxExpirationDay(fridge) + 1
    #creates lenght of histogram
    for place in range(places):
        histogram.append(0)
    #adds 1 if the food expiration = to the index of histogram
    for food in fridge:
        histogram[food.expiration] += 1
    return histogram


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]

"""
Task #3
"""

#get the sum of all items from list from index start
def listSum(list,start):
    sum = 0
    counter = -1
    for i in list:
        counter += 1
        if counter <= start:
            sum += i
    return sum

def cumulativeSum(histogram):
    sum = []
    for places in range(len(histogram)):
        sum.append(0)
    for i in range(len(sum)):
        sum[i] = listSum(histogram, i)
    return sum

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""

#removes all zeroes from a list
def removeZero(list):
    for i in list:
        if i == 0:
            list.remove(i)
    return list

def sortFoodInFridge(fridge):
    newFridge = fridge.copy()
    sorted = []
    cumulativeS = cumulativeSum(histogramOfExpirations(fridge))
    if len(fridge) == 0:
        return []
    for food in fridge:
        exp = food.expiration
        cumulativeS[exp] = cumulativeS[exp] -1
        posInd = cumulativeS[exp]
        newFridge[posInd] = food
    return newFridge


# test vypisu - pri odevzdani smazte, nebo zakomentujte
openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    lenght = len(fridge)
    reversedFridge = []
    counter = lenght
    for i in range(lenght):
        reversedFridge.append(0)
    for food in fridge:
        reversedFridge[counter-1] = food
        counter -= 1
    return reversedFridge
    # print(reversedFridge)
    # openFridge(reversedFridge)


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    newFridge = fridge.copy()
    sameFood = []
    for food in newFridge:
        if food.name == name:
            sameFood.append(food)
    if len(sameFood) == 0:
        return newFridge
    if len(sameFood) == 1:
        newFridge.remove(sameFood[0])
        return newFridge
    #find food with shortest expiration
    temp = Food(None, float('inf'))
    for food in sameFood:
        if food.expiration < temp.expiration:
            temp = food
    newFridge.remove(temp)
    return newFridge



# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3)]))

# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
