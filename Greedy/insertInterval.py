intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

def insertInterval(intervals, newInterval):
    result = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    result.append(newInterval)
    return result


print(insertInterval(intervals, newInterval))
