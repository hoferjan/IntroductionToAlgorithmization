def insertSort(array):
   for i in range(1, len(array)):
     currentvalue = array[i]
     position = i
     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position - 1]
         position = position-1
     array[position]=currentvalue

arrayToSort = [26,81,54,1,93,65,58,74,36,18,9,95,75,58,61,42]
insertSort(arrayToSort)
print(arrayToSort)