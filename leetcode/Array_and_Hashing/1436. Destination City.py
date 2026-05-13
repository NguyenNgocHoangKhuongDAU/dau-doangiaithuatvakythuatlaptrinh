class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        starts = set()

        for a, b in paths:
            starts.add(a)

        for a, b in paths:
            if b not in starts:
                return b