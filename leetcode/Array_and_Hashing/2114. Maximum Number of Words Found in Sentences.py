class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = 0

        for s in sentences:
            ans = max(ans, len(s.split()))

        return ans