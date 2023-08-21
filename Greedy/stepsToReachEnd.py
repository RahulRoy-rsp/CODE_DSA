nums = [2, 3, 1, 1, 4]

def stepsToReachEnd(nums):
    jumps = 0
    curr  = last = 0
    
    for i in range(len(nums)):
        last = max(last, i + nums[i])
        if i == curr:
            jumps += 1
            curr = last
    
    return jumps
    
print(stepsToReachEnd(nums))
