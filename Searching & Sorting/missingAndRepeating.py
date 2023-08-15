arr = [2, 3, 5, 5, 6, 4]

from collections import Counter

def missingAndRepeating(arr):
    counts = Counter(arr)
    missing, repeating = float('inf'), float('inf')

    for i, j in counts.items():
        if j > 1:
            repeating = i
            break
    
    for i in range(1, max(arr)+1):
        if i not in arr:
            missing = i
            return(missing, repeating)
            
    return max(arr)+1, repeating
    
print(missingAndRepeating(arr))
