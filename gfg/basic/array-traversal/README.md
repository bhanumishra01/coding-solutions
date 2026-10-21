# Array or List Traversal

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[]** of size n that contains integers. Print the elements of the array in a single line with a space between them.

 **Note:**  Don't add a new line at the end.

 **Examples:** 

```
Input: arr[] = [54, 43, 2, 1, 5]
Output: 54 43 2 1 5
Explanation: Just traverse and print the numbers.
```

```
Input: arr[] = [324, 5, 2, 2]
Output: 324 5 2 2
Explanation: Just traverse and print the numbers.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T11:24:18.729Z  

```py
class Solution:
    def arrayTraversal(self, arr: list[int]) -> None:
        n=len(arr)
        for i in range(0,n):
            print(arr[i], end=" ")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/array-traversal/1)