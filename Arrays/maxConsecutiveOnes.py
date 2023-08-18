nums = [1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 5]

def maxConsOnes(nums):
    maxi = 0
    curr = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            curr += 1
        else:
            curr = 0
        maxi = max(maxi, curr)
    
    return maxi
        

print(maxConsOnes(nums))
