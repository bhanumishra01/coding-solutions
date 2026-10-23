# Set Matrix Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

 

 **Example 1:** 

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

```

 **Example 2:** 

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```

 

 **Constraints:** 

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -231 <= matrix[i][j] <= 231 - 1

 

 **Follow up:** 

- A straightforward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 69.07%)  
**Memory:** 20.6 MB (beats 97.91%)  
**Submitted:** 2026-10-23T18:00:39.950Z  

```py
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        col0 = 1 
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if j == 0:
                        col0 = 0  
                    else:
                        matrix[0][j] = 0 
                        matrix[i][0] = 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        for j in range(c - 1, 0, -1):
            if matrix[0][0] == 0:
                matrix[0][j] = 0
        for i in range(0, r):
            if col0 == 0:
                matrix[i][0] = 0
```

---

[View on LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)