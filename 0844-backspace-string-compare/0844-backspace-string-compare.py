class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        backspaces_s = 0
        backspaces_t = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    backspaces_s += 1
                    i -= 1
                elif backspaces_s > 0:
                    backspaces_s -=1
                    i -=1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    backspaces_t += 1
                    j -= 1
                elif backspaces_t > 0:
                    backspaces_t -=1
                    j-=1
                else:
                    break
            
            if i < 0 and j < 0:
                return True

            if i < 0 or j < 0:
                return False

            if s[i] != t[j]:
                return False
            i -=1
            j -=1
        return True