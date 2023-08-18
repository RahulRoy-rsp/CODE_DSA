num = 54612

# Approach 1
def countDigits(num):
    return len(str(num))

print(countDigits(num))

# Approach 2
def countDigits(num):
    digits = 0
    while num >= 1:
        num /= 10
        digits += 1
    return digits

print(countDigits(num))
