class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages=[]
        while len(nums)!=0:
            min_num=min(nums)
            max_num=max(nums)
            averages.append(float(min_num+max_num)/2)
            nums.remove(min_num)
            nums.remove(max_num)
            print(averages)
        return min(averages)    
