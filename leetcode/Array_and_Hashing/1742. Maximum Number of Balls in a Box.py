class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box = {}

        for i in range(lowLimit, highLimit + 1):
            s = sum(int(d) for d in str(i))

            box[s] = box.get(s, 0) + 1

        return max(box.values())