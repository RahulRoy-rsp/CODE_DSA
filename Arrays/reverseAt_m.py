arr = [12, 13, 15, 16, 54, 56, 1]
m = 4


def reverseArr(arr, m):
    left = m + 1
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


print(reverseArr(arr, m))
