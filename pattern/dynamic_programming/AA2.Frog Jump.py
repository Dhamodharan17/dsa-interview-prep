class Solution:
    def minCost(self, height):
        
        def function(i):
            
            if cache[i] != -1:
                return cache[i]
                    
            if i == 0:
                return 0
            
            if i == 1:
                return abs(height[1] - height[0])
            
            jump1 = abs(height[i] - height[i-1]) + function(i-1)
            
            jump2 = abs(height[i] - height[i-2]) + function(i-2)
            
            cache[i] = min(jump1, jump2)
            
            return cache[i]
        
        n = len(height)
        cache = [-1] * n
        return function(n-1)

class Solution:
    def minCost(self, height):
    
        n = len(height)
        
        if n == 0 or n == 1:
            return 0
            
        cache = [0] * n
        cache[1] = abs(height[0] - height[1])
        
        for i in range(2, n):
            jump1 = abs(height[i] - height[i-1]) + cache[i-1]
            jump2 = abs(height[i] - height[i-2]) + cache[i-2]
            cache[i] = min(jump1, jump2)
            
        return cache[n-1]
