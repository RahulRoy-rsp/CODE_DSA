arr = [6, 3, 1, 5, 1]

def nextGreatest(arr):
    result = [-1] * len(arr)
    st = []
 
    for i in range(len(arr)):
        while st and arr[st[-1]] < arr[i]:
            result[st[-1]] = arr[i]
            st.pop()
        st.append(i)
    
    return result


print(nextGreatest(arr))
