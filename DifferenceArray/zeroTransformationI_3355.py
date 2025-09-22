class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        differenceArray = [0]*len(nums)
        sum = 0
        j = 0
        for i in range(len(nums)):
            while differenceArray[i]+sum<nums[i] and j<len(queries):
                  [l,r] = queries[j]
                  if r >= i:
                    differenceArray[max(i,l)]+=1
                    if r+1<len(nums):
                        differenceArray[r+1]-=1
                  j+=1
            if differenceArray[i]+sum>=nums[i]:
                sum+=differenceArray[i]
            elif j== len(queries):
                return False
        return True

        