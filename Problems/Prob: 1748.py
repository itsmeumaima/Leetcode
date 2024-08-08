class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    lst.append(nums[i])
        ans=[i for i in nums if i not in lst]
        return sum(ans)       
