class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        seen=set()
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
        for key,value in d.items():
            if value in seen:
                return False
            seen.add(value)
        return True