class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        revr=s[::-1].replace(" ","").lower()
        revr=re.sub(r'[^a-zA-Z0-9]','',revr)
        s=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        if(s==revr):
            return True
        else:
            return False    