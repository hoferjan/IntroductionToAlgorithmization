# Calculates the probability of 'lucky' public ticket number occurence
# Tickets with a 6 digit serial number are considered 'lucky'
# when the sum of first and last 3 digits of the serial number are equal  

class LuckyNumberCounter:

  def __init__(self, digitCount):
    self.digitCount = digitCount
    self.numberCount = 1

  # as many methods as you need...

  def isLuckyNumber(self, number):
      first_half = number // (10)**((len(str(number)))/2)
      second_half = number - (first_half * 10 **((len(str(number)))/2))
      first_half_sum = 0
      second_half_sum = 0
      first_half = str(first_half)
      first_half = list(first_half)
      second_half = str(second_half)
      second_half = list(second_half)
      for num in first_half:
          first_half_sum += int(num)
      for num in second_half:
          second_half_sum += int(num)
      if second_half_sum == first_half_sum:
          return True
      else:
          return False

  def getLuckyNumberCount(self):
        if self.digitcount // 2 == 0:
            return None
        else:
            pass # tady dopis funkci


# digits = 6
# lnc = LuckyNumberCounter(digits)
# luckyNumbersTotal = lnc.getLuckyNumberCount()
# luckyNumbersProbab = luckyNumbersTotal / lnc.numberCount
#
# print(lnc.digitCount, "digit lucky numbers count:", luckyNumbersTotal)
# print("Probability of getting a lucky number is:", luckyNumbersProbab, end=" ")
# print("so chance is 1 in", 1 / luckyNumbersProbab)


def isLuckyNumber(number):
    first_half = number//1000
    second_half = number - (first_half*1000)
    first_half_sum = 0
    second_half_sum = 0
    first_half = str(first_half)
    first_half = list(first_half)
    second_half = str(second_half)
    second_half = list(second_half)
    for num in first_half:
        first_half_sum += int(num)
    for num in second_half:
        second_half_sum +=int(num)
    if second_half_sum == first_half_sum:
        return True
    else:
        return False

print(isLuckyNumber(111111))
print(len(str(99)))