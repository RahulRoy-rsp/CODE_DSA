stri = "{([])}"

def balancedParenthesis(stri):
    mySt = []
    
    for i in range(len(stri)):
        if stri[i] == '(' or stri[i] == '{' or stri[i] == '[':
            mySt.append(stri[i])
        else:
            if stri[i] == ')' and mySt.pop() != '(':
                return False
            if stri[i] == '}' and mySt.pop() != '{':
                return False
            if stri[i] == ']' and mySt.pop() != '[':
                return False
    
    if len(mySt) == 0:
        return True
    else:
        return False


print(balancedParenthesis(stri))
