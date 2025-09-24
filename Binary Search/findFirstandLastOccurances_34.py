class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.searchFirst(nums,target)
        if  first==-1:
            return [-1,-1]
        last = self.searchLast(nums,target)
        return [first, last]

    def searchFirst(self,nums, target):
        l = 0
        h = len(nums)-1
        res = -1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                if mid==0  or nums[mid-1] != target:
                    return mid
                else:
                    h = mid-1
            elif nums[mid] < target:
                    l = mid+1
            else:
                    h = mid-1

        return res

    def searchLast(self,nums, target):
        l = 0
        h = len(nums)-1
        res = -1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                if mid==len(nums)-1 or nums[mid+1] != target:
                     return mid
                else:
                    l=mid+1
            elif nums[mid] < target:
                    l = mid+1
            else:
                    h = mid-1

        return res

        