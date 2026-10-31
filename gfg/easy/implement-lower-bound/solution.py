class Solution:
    def lowerBound(self, arr, target):
        n=len(arr)
        left=0
        right=len(arr)-1
        ans=n
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>=target:
                ans=mid
                right= mid-1
            else:
                left=mid+1
                
            
        return ans 