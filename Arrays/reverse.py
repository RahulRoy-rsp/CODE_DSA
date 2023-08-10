arr = [12, 21, 12, 1, 3, 4, 5]

# Approach 1
def reverseArr(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

print(reverseArr(arr)

# Approach 2
def reverseArr(arr):
    return arr[::-1]


print(reverseArr(arr))
