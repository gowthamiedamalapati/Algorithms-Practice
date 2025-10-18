class Solution(object):
    def subsets(self, nums):
        res = []
        curr = []

        def backtrack(start):     
            res.append(curr[:])            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        return res
     