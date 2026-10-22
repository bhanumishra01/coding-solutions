class Solution:
    def subarraySum(self, arr):
        total=0
        n=len(arr)
        for i in range(0,n):
            total+=arr[i] * (i + 1) * (n - i)
            
        return total