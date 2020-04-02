# Title: Single Number
# URL: https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        '''            
            a ^ a = 0
            a ^ 0 = a 
            a ^ a ^ b = (a ^ a) ^ b = 0 ^ b = b
        '''
        sum = 0
        for i in nums:
            sum = sum ^ i
        return sum
            
    def singleNumber_2(self, nums):
        '''
        2∗(a+b+c)−(a+a+b+b+c) = c
        '''
        return 2 * sum(set(nums)) - sum(nums
        
