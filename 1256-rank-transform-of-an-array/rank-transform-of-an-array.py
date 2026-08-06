class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(set(arr))
        d={}
        res=[]
        for i in range(len(temp)):
            d[temp[i]]=i+1
        for j in arr:
            res.append(d[j])
        return res