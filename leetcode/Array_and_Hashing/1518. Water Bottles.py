class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles

        while numBottles >= numExchange:
            new = numBottles // numExchange
            total += new
            numBottles = new + (numBottles % numExchange)

        return total