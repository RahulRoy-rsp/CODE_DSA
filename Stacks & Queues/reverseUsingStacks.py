st = "Kacey"

def revUsingStack(st):
    rev = ""
    strStack = list(st)
    for i in range(len(strStack)):
        rev += strStack.pop()
    
    return rev

print(revUsingStack(st))
