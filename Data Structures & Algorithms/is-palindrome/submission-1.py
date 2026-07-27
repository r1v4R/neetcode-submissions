class Solution:
    def isPalindrome(self, s: str) -> bool:
       i,j,f=0,len(s)-1,0
       s=s.lower()
       while i<j:
        while i<j and (s[i].isalnum()==False):
            i=i+1
        while i<j and (s[j].isalnum()==False):
            j=j-1   
        if(s[i]!=s[j]):
            f=1
            return False
        else:
            i=i+1
            j=j-1  
       if(f==0):
        return True