num = "7000452"

# Approach 1
def largestOddNum(num):
    i = len(num) - 1
    while i >= 0:
        if int(num[i])%2:
            return num[:i+1]
        i -= 1
    return "No odd numbers"
    
print(largestOddNum(num))


# Approach 2
def largestOddNum(num):
    if int(num)%2!=0:
            return num
    num = int(num)
    for i in range(len(str(num))):
        if num%2 != 0:
            return str(num)
        else:
            num //= 10
    return "No odd Numbers"

print(largestOddNum(num))
