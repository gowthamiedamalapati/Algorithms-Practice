class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums)==1:
            return nums[0]
        n = len(nums)-1
        low = 0
        hgh = len(nums) - 1
        while low <= hgh:
            m = (low+hgh)//2
            if ((m == 0) or nums[m]!=nums[m-1]) and ( m == len(nums)-1 or nums[m]!=nums[m+1]) :
                return nums[m]
            elif nums[m] == nums[m-1]:
                temp = n-m
                if (n-m)%2==0:
                    hgh = m-1
                else:
                    low = m+1
            elif nums[m] == nums[m+1]:
                if m%2==0:
                    low = m+1
                else:
                    hgh = m-1
        return
        