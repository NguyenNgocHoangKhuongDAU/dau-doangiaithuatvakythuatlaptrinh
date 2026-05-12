class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for char in s[::-1]:
            if char == " ":
                if count > 0:
                    break
            else:
                count +=1
        return count    
