arr = [0, 2, 0, 1, 0, 1]

# Approach 1
def sort012(arr):
    left = 0
    right = len(arr) - 1
    
    i = 0
    while i < len(arr) and i <= right:
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1
    return arr
    
print(sort012(arr))

# Approach 2
def sort012(arr):
    arr.sort()
    return arr
    
print(sort012(arr))

