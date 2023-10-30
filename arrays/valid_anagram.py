'''
TC: O(len_s * log(len_s) + len_t + log(len_t))
SC: O(n)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

'''
TC: O(n)
SC: O(1)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq, t_freq = [0]*26, [0]*26

        for index in range(len(s)):
            s_freq[ord(s[index]) - ord("a")] += 1
            t_freq[ord(t[index]) - ord("a")] += 1

        return s_freq == t_freq