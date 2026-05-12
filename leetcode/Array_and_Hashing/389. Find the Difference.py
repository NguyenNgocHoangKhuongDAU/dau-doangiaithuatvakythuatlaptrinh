class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cs = Counter(s)
        ct = Counter(t)

        for ch in ct:
            if ct[ch] != cs[ch]:
                return ch