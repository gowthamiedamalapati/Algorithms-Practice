class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        curr_max = nums[0]
        curr_mn = nums[0]
        temp_max = curr_max
        temp_mn = curr_mn
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                curr_max = max(nums[i],nums[i]*curr_max)
                curr_mn = min(nums[i],nums[i]*curr_mn)
            else:
                curr_max = max(nums[i],nums[i]*temp_mn)
                curr_mn = min(nums[i],nums[i]*temp_max)
            temp_max = curr_max
            temp_mn = curr_mn
            max_product = max(max_product,curr_max)
        return max_product
