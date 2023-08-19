s = "(()())(())"

def removeOuterPar(s):
    res, opened = [], 0
    for c in s:
        if c == '(' and opened > 0:
            res.append(c)
        if c == ')' and opened > 1:
            res.append(c)
        if c == '(':
            opened += 1 
        else:
            opened -= 1
    
    return "".join(res)
        
print(removeOuterPar(s))
