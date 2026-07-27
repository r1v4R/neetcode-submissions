class Solution:
    def isPalindrome(self, s: str) -> bool:
       i,j=0,len(s)-1
       while i<j:
        while i<j and (self.check(s[i])==False):
            i=i+1
        while i<j and (self.check(s[j])==False):
            j=j-1   
        if(s[i].lower()!=s[j].lower()):
            return False
        else:
            i=i+1
            j=j-1  
       return True
    def check(self,s):
        return (ord('a')<=ord(s)<=ord('z')) or (ord('A')<=ord(s)<=ord('Z')) or (ord('0')<=ord(s)<=ord('9'))
                