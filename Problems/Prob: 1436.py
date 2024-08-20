class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sorces=set()
        city=set()
        for i in paths:
            sorces.add(i[0])
            city.add(i[1])
        for j in city:
            if j not in sorces:
                return j     
