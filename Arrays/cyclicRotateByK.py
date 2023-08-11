arr = [1, 2, 3, 4, 5]
k = 2

# Approach 1
def rotateByK(arr, k):
    new = arr[k+1:] + arr[:k+1]
    return new

print(rotateByK(arr, k))


# Approach 2
def rotateByK(arr, k):
    done = 0
    while done < k+1:
        temp = arr[0]
        arr.remove(temp)
        arr.append(temp)
        done += 1
    
    return arr
        
print(rotateByK(arr, k))
