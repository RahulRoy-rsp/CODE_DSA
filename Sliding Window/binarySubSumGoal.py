nums = [1,0,1,0,1]
goal = 2

# Approach 1
def binarySubSum(nums, goal):
    preSum = [0]
    
    for num in nums:
        preSum.append(preSum[-1] + num)
        
    counts = 0
    preSumCount = {}
    
    for i in preSum:
        if i-goal in preSumCount:
            counts += preSumCount[i-goal]
            
        if i in preSumCount:
            preSumCount[i] += 1
        else:
            preSumCount[i] = 1
    
    return counts

print(binarySubSum(nums, goal))


# Approach 2
def binarySubSum(nums, goal):
    counts = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if sum(nums[i:j]) == goal:
                counts += 1
    
    return counts

print(binarySubSum(nums, goal))
