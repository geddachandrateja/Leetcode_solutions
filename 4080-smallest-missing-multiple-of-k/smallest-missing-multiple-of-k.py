class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        multiple=k
        while multiple in d:
            multiple+=k
        return multiple
