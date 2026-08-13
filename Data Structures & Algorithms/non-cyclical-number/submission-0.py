class Solution:
    def isHappy(self, n: int) -> bool:
        s, f = n, self.sumOfSquares(n)
        
        while s != f:
            f = self.sumOfSquares(f)
            f = self.sumOfSquares(f)
            s = self.sumOfSquares(s)
        return f==1

    def sumOfSquares(self, n):
        output = 0
        while n:
            x = n%10
            output += (x*x)
            n = n//10
        return output
