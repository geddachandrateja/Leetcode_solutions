class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        total=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]==0:
                total-=1
            else:
                total+=1
            if total in d:
                maximum=max(maximum,i- d[total])
            else:
                d[total]=i
        return maximum