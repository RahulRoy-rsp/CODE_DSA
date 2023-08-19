s = "abcde"
goal = "cdeab"

# Approach 1
def isRotated(s, goal):
    fro_ = s.index(goal[0])
    return (s[fro_:] + s[:fro_]) == goal

print(isRotated(s, goal))


# Approach 2
def isRotated(s, goal):
    return len(s) == len(goal) and s in goal+goal

print(isRotated(s, goal))
