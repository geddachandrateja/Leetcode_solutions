class Solution:
    def isHappy(self, n: int) -> bool:
        d=set()
        while n!=1:
            if n in d:
                return False
            d.add(n)
            total=0
            while n!=0:
                digit=n%10
                total+= digit**2
                n//=10
            n=total
        return True