# Title: Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = 0
        b = nums[0]
        for i in nums:
            a = a + i 
            if a > b:
                b = a
            if a < 0:
                a = 0
        return b
