def findKthPositive(self, arr, k):
        if k < arr[0]:
            return k
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] - (mid+1) < k:
                ans = mid
                low = mid+1
            else:
                high = mid -1
        rem = k - (arr[ans]-(ans+1))
        return arr[ans]+rem