class Solution:
    def isPalindrome(self, s: str) -> bool:
       i,j,f=0,len(s)-1,0
       while i<j:
        while i<j and (self.check(s[i])==False):
            i=i+1
        while i<j and (self.check(s[j])==False):
            j=j-1   
        if(s[i].lower()!=s[j].lower()):
            f=1
            return False
        else:
            i=i+1
            j=j-1  
       if(f==0):
        return True
    def check(self,s):
        if((ord('a')<=ord(s)<=ord('z')) or (ord('A')<=ord(s)<=ord('Z')) or (ord('0')<=ord(s)<=ord('9'))):
            return True
        else:
            return False    