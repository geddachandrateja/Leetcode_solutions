class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(numbers)):
            rem=target-numbers[i]
            if rem in d:
                res.append(d[rem]+1)
                res.append(i+1)
            d[numbers[i]]=i
        return res