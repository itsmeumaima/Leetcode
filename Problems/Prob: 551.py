class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent=0
        late=0
        for i in s:
            if i=='A':
                absent+=1
                if absent==2:
                    return False
            if i=='L':
                late+=1
                if late==3:
                    return False
            else:
                late=0
        return True
        
