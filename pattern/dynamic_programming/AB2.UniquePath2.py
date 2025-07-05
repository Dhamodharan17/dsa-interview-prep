class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        M, N = len(obstacleGrid),len(obstacleGrid[0])

        @lru_cache
        def function(i,j):

            if i >= M or j >= N:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if i == M-1 and j == N-1:
                return 1
              
            right = function(i,j+1)
            down = function(i+1,j)

            return right + down
        
        return function(0,0)

        
