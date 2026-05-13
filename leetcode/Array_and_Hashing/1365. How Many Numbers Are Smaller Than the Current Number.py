class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            a.append(count)
        return a