intervals = [[1,3], [1, 3]]

def removeOverlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)

    prev = 0
    count = 1

    for i in range(1, n):
        if intervals[i][0] >= intervals[prev][1]:
            prev = i
            count += 1

    return n - count	

print(removeOverlapping(intervals))
