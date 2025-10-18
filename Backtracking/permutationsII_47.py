class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        path = []
        taken = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and i-1 not in taken:
                    continue
                if i not in taken:
                   taken.add(i)
                   path.append(nums[i])
                   backtrack()
                   taken.remove(i)
                   path.pop()
            return

        
        backtrack()
        return res
        
        