# Max Consecutive Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary array `nums`, return  *the maximum number of consecutive* `1` *'s in the array*.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

```

 **Example 2:** 

```
Input: nums = [1,0,1,1,0,1]
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 17 ms (beats 49.87%)  
**Memory:** 21.8 MB (beats 81.43%)  
**Submitted:** 2026-10-14T16:55:57.853Z  

```py

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for i in nums:
            if i == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)