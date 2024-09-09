class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no=list(set(nums))
        for i in no:
            count=nums.count(i)
            if count>len(nums)/2:
                return i
        
