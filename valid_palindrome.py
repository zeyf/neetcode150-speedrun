class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([char.lower() for char in s if char.isalnum()])
        x, y = 0, len(clean_s)-1

        while x < y:
            if clean_s[x] != clean_s[y]:
                return False
            x, y = x + 1, y - 1
        
        return True