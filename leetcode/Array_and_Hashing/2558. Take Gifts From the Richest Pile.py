class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            biggest = max(gifts)
            index = gifts.index(biggest)

            gifts[index] = int(biggest ** 0.5)

        return sum(gifts)