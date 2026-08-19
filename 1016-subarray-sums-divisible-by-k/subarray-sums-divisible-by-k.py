class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        total_sum=0
        count=0
        for right in range(len(nums)):
            total_sum+=nums[right]
            rem=total_sum%k
            if rem in d:
                count+=d[rem]
            d[rem]=d.get(rem,0)+1
        return count
