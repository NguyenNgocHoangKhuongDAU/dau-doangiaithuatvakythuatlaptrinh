class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        
        total = 0
        
        for x in count:
            if count[x] == 1:
                total += x
                
        return total