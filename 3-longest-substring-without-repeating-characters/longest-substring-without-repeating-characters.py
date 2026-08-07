class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        left=0
        maximum=0
        for right in range(len(s)):
            while s[right] in d:
                del d[s[left]]
                left +=1
            if s[right] not in d:
                d[s[right]]=1
                maximum=max(maximum,right-left+1)
        return maximum