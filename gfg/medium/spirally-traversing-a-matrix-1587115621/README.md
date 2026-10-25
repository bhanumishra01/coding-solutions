# Spirally Traversing Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a rectangular matrix  **mat[][]**  of size  **n x m**, and return a 1D array containing all its elements in  **spiral** order.

 **Examples:** 

```
Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation: 

```

```
Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
Explanation: Applying same technique as shown above.
```

```
Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54].
```

 **Constraints:** 
1 ≤ n, m ≤1000
0 ≤ mat[i][j] ≤100

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T17:11:08.088Z  

```py
class Solution:
    def spirallyTraverse(self, mat):
        n = len(mat)
        m = len(mat[0])

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        ans = []

        while top <= bottom and left <= right:

            # 1. Traverse left to right
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

            # 2. Traverse top to bottom
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            # 3. Traverse right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            # 4. Traverse bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
       
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1)