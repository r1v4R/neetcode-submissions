class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=sorted(nums)
        flag=0
        for i in range(len(n)-1):
            if(n[i]==n[i+1]):
                flag=1
                return True

        if(flag==0):
            return False