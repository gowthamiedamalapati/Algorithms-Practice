class Solution(object):
    def merge(self, intervals):
        new = sorted(intervals, key = lambda x:x[0])
        arr = [new[0]]
        j = 1
        while j < len(new):
            if new[j][0] <= arr[-1][1]:
                arr[-1][1] = max(new[j][1],arr[-1][1])
            else:
                arr.append(new[j])
            j+=1
        return arr
