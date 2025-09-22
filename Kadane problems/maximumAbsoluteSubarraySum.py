class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        curr_max = nums[0]
        curr_min = nums[0]
        max_sub = abs(nums[0])
        for i in range(1,len(nums)):
            curr_max = max(nums[i],curr_max+nums[i])
            curr_min = min(nums[i],curr_min+nums[i])
            max_sub = max(max_sub,max(abs(curr_max),abs(curr_min)))
        return max_sub