from collections import defaultdict

def hasSum(array, sum):   
    count = 0 
    length = len(array);
    for i in range(0, length): 
        for j in range(i + 1, length): 
            if array[i] + array[j] == sum: 
                return True
    return False 

def getElementBreakingRule(array):   
    for index in range(25, len(array)):
        if not hasSum(array[index-25:index], array[index]):
            return (index, array[index])
    return (-1,0)

def getContiguousSet(array, sum): 
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if sum == current_sum:
                return (i,j)
  

with open('./data/data_day09', 'r') as f:
    data = f.readlines()
    array = [int(string.replace('\n', '')) for string in data]
    (invalid_index, invalid_number) = getElementBreakingRule(array) 
    print invalid_number
    (start, end) = getContiguousSet(array, invalid_number)
    print max(array[start:end+1]) + min(array[start:end+1])
     