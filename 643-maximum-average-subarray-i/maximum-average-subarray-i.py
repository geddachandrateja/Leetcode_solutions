class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        maximum=0
        current_avg=0
        for right in range(k):
            current_avg+=nums[right]
        maximum=current_avg/k
        for right in range(k,len(nums)):
            current_avg-=nums[left]
            left+=1
            current_avg+=nums[right]
            maximum=max(maximum,current_avg/k)
        return maximum


