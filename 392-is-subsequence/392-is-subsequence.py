class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        while i < len(s):
            fonud_idx = t.find(s[i])
            if fonud_idx > -1:
                i += 1
                t = t[fonud_idx + 1:]
            else:
                break;
                
        if i == len(s):
            return True
        return False
