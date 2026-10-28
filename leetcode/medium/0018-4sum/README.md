# 4Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` of `n` integers, return  *an array of all the  **unique**  quadruplets*  `[nums[a], nums[b], nums[c], nums[d]]` such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

```

 **Example 2:** 

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 200
- -109 <= nums[i] <= 109
- -109 <= target <= 109

## Solution

**Language:** Python  
**Runtime:** 407 ms (beats 34.24%)  
**Memory:** 19 MB (beats 98.31%)  
**Submitted:** 2026-10-28T13:37:27.372Z  

```py
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n=len(nums)
        result=[]
        nums.sort()
        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                     continue
                k=j+1
                l=n-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total==target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                            
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
                    elif total<target:
                        k+=1
                    else :
                        l-=1
        return result
                        
                        
                    
```

---

[View on LeetCode](https://leetcode.com/problems/4sum/)