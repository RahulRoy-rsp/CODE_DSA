arr = [12, 13, 15, 16, 54, 56, 1]

# Approach 1
def sumMaxMin(arr):
    return max(arr) + min(arr)

print(sumMaxMin(arr))


# Approah 2
def sumMaxMin(arr):
    arr.sort()
    return arr[0] + arr[-1]

print(sumMaxMin(arr))
