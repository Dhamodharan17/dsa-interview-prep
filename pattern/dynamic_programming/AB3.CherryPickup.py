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


#bottom up
class Solution:
    def solve(self, n, m, grid):
        
        # 3d array
        dp = [ [ [ 0 for _ in range(m) ] for _ in range(m) ] for _ in range(n) ]
        
        #base case - independent case
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1] [j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        #subproblem
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    
                    # now p1 in (i, j1) and p2 in (j,j2)
                    # current cost
                    if j1 == j2:
                        ans = grid[i][j1]
                    else:
                        ans = grid[i][j1] + grid[i][j2]
                        
                    # find best previous, we would use.
                    maxi = float('-inf')
                    #all positions i and j could have come from.
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            new_j1 = j1+di
                            new_j2 = j2+dj
                            
                            if 0<=new_j1<m and 0<=new_j2<m:
                                maxi = max(maxi,dp[i+1][new_j1][new_j2])
                                
                    dp[i][j1][j2] = maxi + ans
                    

        return dp[0][0][m-1] 

