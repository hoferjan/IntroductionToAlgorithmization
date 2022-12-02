def permutations(array):
    if len(array) == 0 or len(array) == 1:
        return [array]
    answer = []
    for i in range(len(array)):
        for j in permutations(array[:i] + array[i+1:]):
            answer.append([array[i]] + [j])
    flattened = flatten(answer)
    divided = divide(flattened, len(array))
    return divided

#function that reuturns all items in list of lists
def flatten(array):
    answer = []
    for i in array:
        if type(i) == list:
            answer += flatten(i)
        else:
            answer.append(i)
    return answer

#function that divides items of list into list of lists with length of n
def divide(array, n):
    answer = []
    for i in range(0, len(array), n):
        answer.append(array[i:i+n])
    return answer

print(permutations([1,2,3]))

print(permutations([1,2,3,4]))