# Sum of Subarrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**, find the  **sum** of all the **subarrays**  of the given array.

 **Note:** It is guaranteed that the total sum will fit within a 32-bit integer range.

 **Examples:** 

```
Input: arr[] = [1, 2, 3] 
Output: 20
Explanation: All subarray sums are: [1] = 1, [2] = 2, [3] = 3, [1, 2] = 3, [2, 3] = 5, [1, 2, 3] = 6. Thus total sum is 1 + 2 + 3 + 3 + 5 + 6 = 20.
```

```
Input: arr[] = [1, 3]
Output: 8
Explanation: All subarray sums are: [1] = 1, [3] = 3, [1, 3] = 4. Thus total sum is 1 + 3 + 4 = 8.
```

 **Constraints :** 
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T12:51:15.857Z  

```py
class Solution:
    def subarraySum(self, arr):
        total=0
        n=len(arr)
        for i in range(0,n):
            total+=arr[i] * (i + 1) * (n - i)
            
        return total
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-subarrays2229/1)