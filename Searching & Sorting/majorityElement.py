arr = [2, 2, 4, 5]


def majorityElement(arr):
    if len(arr) == len(set(arr)):
        return -1
    
    numsCount = {}
    for i in arr:
        if i not in numsCount:
            numsCount[i] = 1
        else:
            numsCount[i] += 1
    
    for i, j in numsCount.items():
        if j > len(arr)//2:
            return i
            
    return -1
    
print(majorityElement(arr))
