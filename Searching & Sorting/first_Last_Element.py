nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
k = 5

# Approach 1: 
def searchFirst(nums, k):
    left = 0
    right = len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left+right)//2
        
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] > k:
            right = mid - 1
        else:
            ans = mid
            right = mid - 1
        
    return ans

def searchLast(nums, k):
    left = 0
    right = len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left+right)//2
        
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] > k:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
        
    return ans
    
first = searchFirst(nums, k)
second = searchLast(nums, k)

print(first, second)



# Approach 2: 
def searchFirstAndLast(nums, k):
    dict_ = {}
    for i in range(len(nums)):
        if nums[i] not in dict_:
            dict_[nums[i]] = [i]
        else:
            dict_[nums[i]] += [i]
            
    for i, j in dict_.items():
        if i == k:
            return j[0], j[-1]
    
    return -1, -1

print(searchFirstAndLast(nums, k))
