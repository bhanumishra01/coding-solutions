class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total=nums[0]
        maxSubArray=nums[0]
        for i in range(1,len(nums)):
            total=max(nums[i],total+nums[i])
            maxSubArray=max(maxSubArray,total)
        return maxSubArray
        