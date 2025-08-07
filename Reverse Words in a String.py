class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split input by space so you have an array of words [the, sky, is, blue]
        # but we can call .reverse

        result = s.split()
        result.reverse()
        return " ".join(result)
        # Space O(N)
        # Runtime O(N)