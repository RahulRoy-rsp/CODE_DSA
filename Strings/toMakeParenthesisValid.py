s = "(("
def minAddToMakeValid(s):
    st = []
    counter = 0
    
    for i in s:
        if i == "(":
            st.append(i)
        else:
            if st and st[-1]:
                st.pop()
            else:
                counter += 1
    return counter + len(st)

print(minAddToMakeValid(s))
