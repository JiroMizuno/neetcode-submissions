import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(s.maketrans("","",string.punctuation+string.whitespace)).lower()
        n = len(s)
        mid = n//2
        for i in range(mid):
            if s[i] != s[n-1-i]: return False
        return True

