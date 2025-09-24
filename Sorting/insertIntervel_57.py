class Solution(object):
    def insert(self, intervals, newInterval):
        arr = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                arr.append(newInterval)
                return arr+intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                arr.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        arr.append(newInterval)
        return arr

                                  