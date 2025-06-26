class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        "With approaching this problem you would need to use a hashmap"
        freq_s = {}
        freq_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        
        return freq_s == freq_t