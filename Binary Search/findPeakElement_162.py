class Solution(object):
    def findPeakElement(self, nums):
        l=0
        h=len(nums)-1
        while l <= h:
            m =(l+h)//2
            if (m==0 or nums[m-1] < nums[m]) and (m==len(nums)-1 or nums[m]>nums[m+1]):
                return m
            elif m>0 and nums[m-1] >= nums[m]:
                h = m-1
            else:
                l = m+1
        return -1

