arr = [7, 10, 4, 3, 20, 15]
k = 3

def kSmallLarge(arr, k):
    arr.sort()
    return arr[k-1], arr[-k-1]

print(kSmallLarge(arr, k))
