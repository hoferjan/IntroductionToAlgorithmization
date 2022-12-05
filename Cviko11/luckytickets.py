# Calculates the probability of 'lucky' public ticket number occurence
# Tickets with a 6 digit serial number are considered 'lucky'
# when the sum of first and last 3 digits of the serial number are equal  

class LuckyNumberCounter:

  def __init__(self, digitCount):
    self.digitCount = digitCount
    self.numberCount = (10 **digitCount) - 1

  # as many methods as you need...

  def isLuckyNumber(self, number):
      first_half_sum = 0
      second_half_sum = 0
      first_half = number.copy()
      second_half = number.copy()
      for i in range(len(number)//2):
          first_half.pop()
          second_half.pop(0)
      for num in first_half:
          first_half_sum += int(num)
      for num in second_half:
          second_half_sum += int(num)
      if second_half_sum == first_half_sum:
          return True
      else:
          return False
  def getLuckyNumberCount(self):
    sum = 0
    if self.digitCount % 2 != 0:
        return None
    for number in range(self.numberCount+1):
        number = list(str(number))
        while len(number) != self.digitCount:
            number.insert(0,"0")
        if self.isLuckyNumber(number):
            sum +=1
        print(number)
    return sum


digits = 6
lnc = LuckyNumberCounter(digits)
luckyNumbersTotal = lnc.getLuckyNumberCount()
luckyNumbersProbab = luckyNumbersTotal / lnc.numberCount

print(lnc.digitCount, "digit lucky numbers count:", luckyNumbersTotal)
print("Probability of getting a lucky number is:", luckyNumbersProbab, end=" ")
print("so chance is 1 in", 1 / luckyNumbersProbab)


