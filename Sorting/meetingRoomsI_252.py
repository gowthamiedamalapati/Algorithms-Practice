class Solution(object):
    def canAttendMeetings(self, intervals):
        if len(intervals)==0:
            return True
        new = sorted(intervals, key = lambda x:x[0])
        arr = [new[0]]
        j = 1
        while j < len(new):
            if new[j][0] < arr[-1][1]:
                return False
            else:
                arr.append(new[j])
                j+=1
        return True
