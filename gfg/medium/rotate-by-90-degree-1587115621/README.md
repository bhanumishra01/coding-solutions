# Rotate by 90 degree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a square matrix  **mat** [][] of size  **n x n**. The task is to rotate it by **90 degrees**  in an **anti-clockwise**  direction without using any extra space. 

 **Examples:** 

```
Input: mat[][] = [[0, 1, 2], 
                [3, 4, 5], 
                [6, 7, 8]] 
Output: [[2, 5, 8],
        [1, 4, 7],
        [0, 3, 6]]
```

```
Input: mat[][] = [[1, 2],
                [3, 4]]
Output: [[2, 4],
        [1, 3]]

```

 **Constraints:** 
1 ≤ n ≤ 102
0 ≤ mat[i][j] ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T18:14:05.710Z  

```py
class Solution:
    def rotateMatrix(self, mat):
        n=len(mat)
        for i in range(0,n-1):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for i in range(0,n):
            mat.reverse()
            return mat
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1)