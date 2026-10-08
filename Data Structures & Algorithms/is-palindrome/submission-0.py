import string
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()   
        punc = string.punctuation
        pattern = r"[\s{}]".format(punc)
        s = re.sub(pattern, "", s)
        n = len(s)
        mid = n//2
        for i in range(mid):
            if s[i] != s[n-1-i]: return False
        return True
        