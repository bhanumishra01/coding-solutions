# Implement Lower Bound

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array  **arr[]** (following 0-based indexing) and a number  **target**, find the lower bound of the target in this given array.

- The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.
- If all the elements in the given array are smaller than the target, the lower bound will be the length of the array. 

 **Examples :** 

```
Input:  arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3
Explanation: 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.
```

```
Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 11
Output: 4
Explanation: 4 is the smallest index in arr[] where element (arr[4] = 11) is greater than or equal to 11.

```

```
Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 100
Output: 7
Explanation: As no element in arr[] is greater than 100, return the length of array.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T18:21:11.134Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/implement-lower-bound/1)