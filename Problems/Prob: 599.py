class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {}
        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                index_sum = i + list2.index(restaurant)
                index_map[restaurant] = index_sum
        min_sum = min(index_map.values())
        result = [restaurant for restaurant, index_sum in index_map.items() if index_sum == min_sum]
        
        return result
