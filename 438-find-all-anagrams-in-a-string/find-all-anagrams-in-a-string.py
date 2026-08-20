class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        res=[]
        d={}
        for i in p:
            d[i]=d.get(i,0)+1
        d1={}
        for right in range(len(s)):
            d1[s[right]]=d1.get(s[right],0)+1
            if right-left+1 >len(p):
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    del d1[s[left]]
                left+=1
            if d==d1:
                res.append(left)
        return res