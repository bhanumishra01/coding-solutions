class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        positive,negative=0,1
        for i in range(0,n):
            if nums[i]>=0:
                result[positive]=nums[i]
                positive += 2
            else:
                result[negative]=nums[i]
                negative += 2
        return result
        def rearrangeArray(self, nums: list[int]) -> list[int]:
            self.rearrangeArray

        