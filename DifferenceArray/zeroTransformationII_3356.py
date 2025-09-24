class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        differenceArray = [0]*len(nums)
        sum = 0
        j = 0
        for i in range(len(nums)):
            while differenceArray[i]+sum<nums[i] and j < len(queries):
                [l,r,val] = queries[j]
                if r>=i:
                  differenceArray[max(l,i)]+=val
                  if r+1 < len(nums):
                    differenceArray[r+1]-=val
                j+=1
            if differenceArray[i]+sum>=nums[i]:
                sum += differenceArray[i]  
            elif differenceArray[i]+sum<nums[i] and j == len(queries):
                    return -1
        return j
