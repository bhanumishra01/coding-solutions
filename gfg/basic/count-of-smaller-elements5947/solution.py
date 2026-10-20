class Solution:
    def countOfElements(self, x, arr):
        # code here
        countOfElements=0
        n=len(arr)
        
        for i in range(0,n):
            if arr[i]<=x:
                countOfElements+=1
                
        return countOfElements

