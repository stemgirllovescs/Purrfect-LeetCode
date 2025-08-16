class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)

        # O(N log N) for runtime
        # O(N) for space because sorted() in python creates a new list

        # char to integer 
        # for instance, 'a" to 1
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')] += 1
            tCount[ord(t[i]) - ord('a')] += 1
        
        return sCount == tCount

        # O(N) for runtime
        # O(1) for space because 26 letters
