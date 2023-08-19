nums = [1,0,1,0,1]
goal = 2

def binarySubSum(nums, goal):
    counts = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if sum(nums[i:j]) == goal:
                counts += 1
    
    return counts

print(binarySubSum(nums, goal))
