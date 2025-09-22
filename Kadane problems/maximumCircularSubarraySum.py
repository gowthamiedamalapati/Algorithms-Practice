class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        minSub = nums[0]
        maxSub = nums[0]
        currmx = nums[0]
        currmn = nums[0]
        for i in range(1,len(nums)):
            currmx = max(nums[i],nums[i]+currmx)
            currmn = min(nums[i],nums[i]+currmn)
            maxSub = max(maxSub,currmx)
            minSub = min(minSub,currmn)
            total += nums[i]
        circularSum = total - minSub
        if total == minSub:
            return maxSub
        return max(maxSub,circularSum)
