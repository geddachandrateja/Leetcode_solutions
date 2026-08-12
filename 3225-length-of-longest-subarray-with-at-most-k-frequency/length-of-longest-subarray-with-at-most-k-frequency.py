class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maximum=0
        left=0
        d={}
        for right in range(len(nums)):
            d[nums[right]]=d.get(nums[right],0)+1
            while d[nums[right]]>k:
                d[nums[left]]-=1
                left+=1
            maximum=max(maximum,right-left+1)
        return maximum