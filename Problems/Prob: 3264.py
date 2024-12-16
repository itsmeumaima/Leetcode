class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            minelement=min(nums)
            new=minelement*multiplier
            for i in range(len(nums)):
                if (nums[i]==minelement):
                    nums[i]=new
                    break
        return nums
