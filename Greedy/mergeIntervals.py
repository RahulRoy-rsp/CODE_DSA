intervals = [[1,3],[2,6],[8,10],[15,18]]

def mergeIntervals(intervals):
	intervals.sort()
	ans = []
	curr = intervals[0]
	for i in intervals:
	    if i[0] <= curr[1]:
	        curr[1] = max(curr[1], i[1])
	    else:
	        ans.append(curr)
	        curr = i
	ans.append(curr)
	return ans
	
print(mergeIntervals(intervals))
