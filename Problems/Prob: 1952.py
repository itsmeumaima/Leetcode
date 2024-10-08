class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 2:
            return False
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
            if count > 3:
                return False
        return count == 3
