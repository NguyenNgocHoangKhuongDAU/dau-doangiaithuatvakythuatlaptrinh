class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        return len(set(count.values())) == 1