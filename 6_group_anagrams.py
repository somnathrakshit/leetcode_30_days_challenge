# Title: Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = ''.join(sorted(s))
            if t in d:
                d.get(t).append(s)
            else:
                d[t] = [s]
        return list(d.values())
