class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d={0:1}
        odd=0
        count=0
        for i in range(len(nums)):
            if nums[i]%2==1:
                odd+=1
            if (odd-k) in d:
                count+=d[odd-k]
            d[odd]=d.get(odd,0)+1
        return count