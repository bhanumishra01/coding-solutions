# Maximum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return  *its sum*.

 

 **Example 1:** 

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

 **Example 2:** 

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

 **Example 3:** 

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution using the  **divide and conquer**  approach, which is more subtle.

## Solution

**Language:** Python  
**Runtime:** 38 ms (beats 50.88%)  
**Memory:** 31.2 MB (beats 93.49%)  
**Submitted:** 2026-10-19T13:08:08.348Z  

```py
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total=nums[0]
        maxSubArray=nums[0]
        for i in range(1,len(nums)):
            total=max(nums[i],total+nums[i])
            maxSubArray=max(maxSubArray,total)
        return maxSubArray
        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray/)