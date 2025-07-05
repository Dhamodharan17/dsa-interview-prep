class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)-1
        if N == 0:
            return nums[0]
        @lru_cache
        def function(i):
            #ignore 1st house
            if i <= 0:
                return 0
            rob = nums[i] + function(i-2)
            skip = function(i-1)
            return max(rob,skip)
        @lru_cache
        def function2(i):
            
            if i < 0:
                return 0
            rob = nums[i] + function2(i-2)
            skip = function2(i-1)
            return max(rob,skip)

        round1 = function(N)
        #ignore last house
        round2 = function2(N-1)    

        return max(round1, round2)

