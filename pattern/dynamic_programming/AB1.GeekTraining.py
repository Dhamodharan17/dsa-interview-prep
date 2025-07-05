from functools import lru_cache
class Solution:
    def maximumPoints(self, arr):
        
        N = len(arr)
        
        @lru_cache
        def function(current_day, prev_activity):
            
            if current_day == N:
                return 0
            
            maxi = -10**9
            #return max of 3 activities like frog have 3 jumps
            for i in range(3):
                
                if prev_activity == i: continue
                                                # move next day, change prev
                cur_cost = arr[current_day][i] + function(current_day+1,i)
                maxi = max(maxi, cur_cost)
            
            return maxi
                
            
        return function(0,-1)
            
class Solution:
    def maximumPoints(self, arr):
        
        N = len(arr)
        
        dp = [[0 for _ in range(3)] for i in range(N)]
        
        #day 1 task
        for i in range(3):
            dp[0][i] = arr[0][i]
            
        
        for day in range(1, N):#each day
            for task in range(3):#each task
                max_prev = 0
                for prev in range(3):#consider each prev
                    if task == prev:continue
                    max_prev = max(max_prev, dp[day-1][prev])
                dp[day][task] = arr[day][task] + max_prev
        
        return max(dp[N-1][0],dp[N-1][1],dp[N-1][2])
        
