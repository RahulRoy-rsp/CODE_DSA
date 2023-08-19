nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

def niceSubArray(nums, k):
    oddCount = 0
    ans = 0
    i = 0
    count = 0
    for j in nums:
        if j % 2 == 1:
            oddCount += 1
            count = 0

        while oddCount==k:
            if nums[i] % 2 == 1:
                oddCount -= 1
            i += 1
            count += 1
            
        ans += count
    return ans

print(niceSubArray(nums, k))
