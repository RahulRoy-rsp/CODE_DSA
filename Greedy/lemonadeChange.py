bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

def lemonadeChange(bills):
    
    coins = {5: 0, 10: 0}
    
    for i in bills:
        if i == 5:
            coins[i] += 1
        
        elif i == 10:
            if coins[5] > 0:
                coins[i] += 1
                coins[5] -= 1
            else:
                return False
        
        elif i == 20:
            if coins[10] > 0 and coins[5] > 0:
                coins[5] -= 1
                coins[10] -= 1
            elif coins[5] > 2:
                coins[5] -= 3
            else:
                return False
                
    return True
    

print(lemonadeChange(bills))
