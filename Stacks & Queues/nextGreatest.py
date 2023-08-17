arr = [6, 3, 1, 5, 1]

# Approach 1
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


# Approach 2
def nextGreatest(arr):
    n = len(arr)
    result = [-1] * n
    st = []
 
    for i in reversed(range(n)):
        while st:
            if st[-1] <= arr[i]:
                st.pop()
            else:
                result[i] = st[-1]
                break
        st.append(arr[i])
    return result


print(nextGreatest(arr))
