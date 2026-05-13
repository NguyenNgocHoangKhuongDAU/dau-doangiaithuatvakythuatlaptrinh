class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = set()

        for c in s:
            if c.isdigit():
                nums.add(int(c))

        nums = sorted(nums)

        if len(nums) < 2:
            return -1

        return nums[-2]