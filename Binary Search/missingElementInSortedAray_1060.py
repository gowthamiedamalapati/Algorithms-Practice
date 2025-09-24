class Solution(object):
    def missingElement(self, nums, k):
        l = 0
        h = len(nums)
        while l < h:
            m = (l+h)//2
            missing = nums[m]-nums[0]-m
            if missing<k:
                l = m+1
            else:
                h = m
        missing_at_lowerbound = nums[l-1]-nums[0]-(l-1)
        rem = k-missing_at_lowerbound
        return nums[l-1]+rem


    #total no of mising till ith index is nums[i]-nums[0]-i
    #we count total number of numbers - existing numbers
    #eg [4,6,8] at index 2(i.e i=2) total number of numbers = nums[i]-nums[0]+1=3(i.e,4,5,6) 
    #existing numbers = i+1
    #missing = (nums[i]-nums[0]+1)-(i+1) = nums[i]-nums[0]-i