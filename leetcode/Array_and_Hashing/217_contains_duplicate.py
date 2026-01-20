class Solution(object):
    def containsDuplicate(self, nums):
        a = []
        for i in nums:
            if i in a:
                return True
            a.append(i)
        return False
    