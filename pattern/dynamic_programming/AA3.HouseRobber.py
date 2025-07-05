class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache
        def function(i):

            if i < 0:
                return 0

            rob = nums[i] + function(i-2)

            skip =  function(i-1)

            return max(rob, skip)   

        n = len(nums)
        return function(n-1)     
