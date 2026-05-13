class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        keo = [0] * num_people
        cho = 1
        i = 0

        while candies > 0:
            keo[i] += min(cho, candies)
            candies -= cho
            cho += 1
            i = (i + 1) % num_people
        
        return keo