class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        new = sorted(intervals, key = lambda x:x[1])
        i = 0
        k = 1
        for j in range(1,len(new)):
            if new[j][0] < new[i][1]:
                continue
            else:
                k+=1
                i=j
        return len(intervals)-k
    