from functools import lru_cache
class Solution:
    def solve(self, n, m, grid):
        
        @lru_cache
        def function(r, i, j):
            
            
            if i >= m or j >= m or i < 0 or j < 0:
                return float('-inf')
            
            if r == n-1:
                if i == j:
                    return grid[r][j]
                else:
                    return grid[r][i] + grid[r][j]
                
            
            maxi = float('-inf')
            #for each robot 1 action
            for di in range(-1,2):
                # there are set of robot 2 actions
                for dj in range(-1,2):
                    
                    val = 0
                    if i == j:
                        val = grid[r][j] + function(r+1, di+i,dj+j)
                    else:
                     #move to next row after eating current 
                        val = grid[r][i] + grid[r][j] + function(r+1, di+i,dj+j)
                    
                    maxi = max(maxi, val)
            
            return maxi
        
        return function(0, 0, m-1)
                    
