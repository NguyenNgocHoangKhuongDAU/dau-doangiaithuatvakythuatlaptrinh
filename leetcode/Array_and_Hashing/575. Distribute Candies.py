class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        loai = len(set(candyType))
        max_keo = len(candyType) // 2

        return min(loai, max_keo)