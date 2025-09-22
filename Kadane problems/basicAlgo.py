class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_sub = nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i],curr_max+nums[i])
            max_sub = max(max_sub,curr_max)
        return max_sub
        