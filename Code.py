class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)
        c = 0
        fc = 0
        for x in nums:
            if x == ma:
                c += 1
            else:
                fc = max(c,fc)
                c = 0
        fc = max(c,fc)
        return fc
            


