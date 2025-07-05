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
