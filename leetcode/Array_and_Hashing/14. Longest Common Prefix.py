class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        Tiento= strs[0]

        for s in strs[1::]:
            while not s.startswith(Tiento):
                Tiento= Tiento[:-1]
                if Tiento == "":
                    return ""
        return Tiento
        