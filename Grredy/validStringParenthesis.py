s = "**))"

def validString(s):
    opened = closed = 0
    for i in s:
        if i == '(':
            opened += 1
            closed += 1
        elif i == ')':
            opened -= 1
            closed = max(closed-1, 0)
        if i == '*':
            opened += 1
            closed = max(closed-1, 0)
        if opened < 0:
            return False
                    
    return closed == 0    
    
print(validString(s))
