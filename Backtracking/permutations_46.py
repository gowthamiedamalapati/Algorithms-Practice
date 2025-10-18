class Solution(object):
    def permute(self, nums):
        res = []
        path = []
        taken = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if nums[i] not in taken:
                    path.append(nums[i])
                    taken.add(nums[i])
                    backtrack()
                    path.pop()
                    taken.remove(nums[i])
            return


        backtrack()
        return res
        