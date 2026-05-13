class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        s = ""

        for c in number:
            if c.isdigit():
                s += c

        res = []

        while len(s) > 4:
            res.append(s[:3])
            s = s[3:]

        if len(s) == 4:
            res.append(s[:2])
            res.append(s[2:])
        else:
            res.append(s)

        return "-".join(res)