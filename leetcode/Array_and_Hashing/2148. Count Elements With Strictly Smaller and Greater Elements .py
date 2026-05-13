class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = min(nums)
        big = max(nums)

        count = 0

        for num in nums:
            if small < num < big:
                count += 1

        return count