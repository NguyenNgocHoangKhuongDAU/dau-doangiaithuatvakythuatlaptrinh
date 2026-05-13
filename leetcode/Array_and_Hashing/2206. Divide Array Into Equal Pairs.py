class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for value in count.values():
            if value % 2 != 0:
                return False

        return True