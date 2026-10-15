# Union of 2 Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two sorted arrays  **a[]**  and  **b[]**, where each array may contain duplicate elements, the task is to return the elements in the union of the two arrays in sorted order. Union of two arrays can be defined as the set containing distinct elements that are present in either of the arrays.

 **Examples:** 

```
Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
```

```
Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: [1, 2, 3, 4, 5]
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
```

```
Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: [1, 2]
Explanation: Distinct elements including both the arrays are: 1 2.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T17:03:34.584Z  

```py
class Solution:
    def findUnion(self, a, b):
            i = 0
            j = 0
            result = []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    if len(result) == 0 or result[-1] != a[i]:
                        result.append(a[i])
                    i += 1
                else:
                    if len(result) == 0 or result[-1] != b[j]:
                        result.append(b[j])
                    j += 1

            while i < len(a):
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1

            while j < len(b):
                if len(result) == 0 or result[-1] != b[j]:
                    result.append(b[j])
                j += 1

            return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1)