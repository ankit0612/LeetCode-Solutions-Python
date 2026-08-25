class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {}
        t_frequency = {}

        for x in range(len(s)):
            s_frequency[s[x]] = s_frequency.get(s[x], 0) + 1

        for x in range(len(t)):
            t_frequency[t[x]] = t_frequency.get(t[x], 0) + 1

        return s_frequency == t_frequency
