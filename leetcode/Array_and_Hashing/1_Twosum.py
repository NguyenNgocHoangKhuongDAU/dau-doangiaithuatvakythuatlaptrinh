class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        num_map = {}

        for i in range(n):
            a = nums[i]
            more = target - a 
            if more in num_map:
                return [i,num_map[more]]

            num_map[a] = i

        return None