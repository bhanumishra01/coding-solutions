# Reverse String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

 **Example 1:** 

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

 **Example 2:** 

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 45.14%)  
**Memory:** 23.5 MB (beats 21.14%)  
**Submitted:** 2026-10-15T17:14:32.456Z  

```py
class Solution:
    def reverseString(self, s: list[str]) -> None:
       s[:]=s[::-1]
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-string/)