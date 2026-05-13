class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        count = {}

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]

                if target in count:
                    count[target] += 1
                else:
                    count[target] = 1

        return max(count, key=count.get)