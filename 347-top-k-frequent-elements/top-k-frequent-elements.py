class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        res=[]
        while k>0:
            max=0
            ele=0
            for key,value in d.items():
                if value>max:
                    max=value
                    ele=key
            res.append(ele)
            del d[ele]
            k-=1
        return res