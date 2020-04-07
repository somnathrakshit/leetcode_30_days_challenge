# Title: Counting Elements
# URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289

class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        c = 0
        for i in arr:
            if (i+1) in s:
                c += 1
        return c
