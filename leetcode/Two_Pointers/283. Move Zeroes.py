class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0

        # đưa tất cả số khác 0 lên đầu
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        # điền 0 vào phần còn lại
        for j in range(i, len(nums)):
            nums[j] = 0
        