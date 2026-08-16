class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words=s1.split()+s2.split()
        res=[]
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        for key,value in d.items():
            if value==1:
                res.append(key)
        return res
            
        
