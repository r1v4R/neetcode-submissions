class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in hashh:
                return [hashh[diff],i]
            hashh[num]=i
        