import sys

inputList = list()
for line in sys.stdin:
    inputList.append(line)

inputList = inputList[0].replace('\n','')
inputList = inputList.split(' ')

for i in range (0,len(inputList)):
    inputList[i] = int(inputList[i])

print inputList

maximumSum = 0
counter = 0

for i in range(0,len(inputList)):
    tmpSum = 0

    for j in range(i,len(inputList)):
        tmpSum += inputList[j]
        if tmpSum > maximumSum:
            maximumSum = tmpSum
    counter = 0
print maximumSum


def mss (lst):
    max_ending_here = max_so_far = 0
    for x in lst:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    
print mss(inputList)
