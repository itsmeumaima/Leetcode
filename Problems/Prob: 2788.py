class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result = []
        
        for word in words:
            parts = word.split(separator)
            result.extend(part for part in parts if part)
        
        return result
