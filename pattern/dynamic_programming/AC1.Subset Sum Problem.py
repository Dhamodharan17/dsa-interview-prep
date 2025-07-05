from functools import lru_cache
class Solution:
    def isSubsetSum (self, arr, sum):
        
        @lru_cache
        def function(i, target):
            
            if target == 0:
                return True
                
            if i >= len(arr):
                return False
            
            pick = False
            if arr[i] <= target:
                pick = function(i+1, target-arr[i])
            
            skip = function(i+1, target)
            
        
            return pick or skip
        
        return function(0, sum)
