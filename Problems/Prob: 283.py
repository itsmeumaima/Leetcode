class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new = [i for i in nums if i != 0]
        size = len(nums) - len(new)
        for i in range(size):
            new.append(0)
        for i in range(len(nums)):
            nums[i] = new[i]
