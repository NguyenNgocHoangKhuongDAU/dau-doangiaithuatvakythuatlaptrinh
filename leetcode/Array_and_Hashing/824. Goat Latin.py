class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        words = sentence.split()
        res = []

        for i in range(len(words)):
            word = words[i]

            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"

            new_word += "a" * (i + 1)
            res.append(new_word)

        return " ".join(res)