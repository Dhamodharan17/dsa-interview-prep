#tabulation(bottom up)
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        cache = [0] * n
        cache[0] , cache[1] = 1, 2

        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n-1]

#recursion (top down)
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
