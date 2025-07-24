class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # HashSet and two pointers, like cutting a cucumber
        # while it's in the hashset, remove that, increment left pointer
        # otherwise add current element to hashset
        result = 0
        hashSet = set()
        left = 0

        for right in range(len(s)):
            # remember to use while because there are duplicated chars in the window
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            result = max(result, right - left + 1)
        return result
        #Runtime O(N)
        #Space O(N), use hashset
