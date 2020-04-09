# Title: Backspace String Compare
# URL: https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sStack = []
        tStack = []
        for s in S:
            if s != '#':
                sStack.append(s)
            elif len(sStack) != 0:
                sStack.pop()
        
        for t in T:
            if t != '#':
                tStack.append(t)
            elif len(tStack) != 0:
                tStack.pop()
        
        while len(sStack) > 0:
            ch = sStack.pop()
            if len(tStack) == 0 or tStack.pop() != ch:
                return False
        
        return len(sStack) == 0 and len(tStack) == 0
