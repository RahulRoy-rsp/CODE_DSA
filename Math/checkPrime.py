num = 8

def checkPrime(num):
    if num <= 1:
        return None
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        

print(checkPrime(num))
