class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        n=len(nums)
        for i in range(n):
            d[nums[i]]=d.get(nums[i],0)+1
        for key,value in d.items():
            if value > n/3:
                res.append(key)
        return res