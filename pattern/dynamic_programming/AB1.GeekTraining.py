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
            
                cur_cost = arr[current_day][i] + function(current_day+1,i)
                maxi = max(maxi, cur_cost)
            
            return maxi
                
            
        return function(0,-1)
            
