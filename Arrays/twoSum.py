nums = [5, 78, 122, 478]
target = 200

# Approach 1
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return "not found"
    
print(twoSum(nums, target))



# Approach 2
def twoSum(nums, target):
    dict_ = {}
    
    for i in range(len(nums)):
        need = target - nums[i]
        if need in dict_:
            return [dict_[need], i]
        dict_[nums[i]] = i
    
    return "not found"
    
print(twoSum(nums, target))
