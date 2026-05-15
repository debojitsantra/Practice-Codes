class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        k = n
        if n < 0:
            n = n*-1
        for i in range(n):
              ans = ans*x
        
        
        if k<0:
            return 1/ans
        else:
            return ans

        
print(Solution().myPow(2, 2))