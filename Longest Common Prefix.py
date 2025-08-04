class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Sort the string first so first and last str are the most different
        strs.sort()
        first = strs[0]
        last = strs[-1]

        index = 0
        result = []
        while index < min(len(first), len(last)) and first[index] == last[index]:
            result.append(first[index])
            index += 1
        
        return "".join(result)

        # Runtime O(N log N * k), where k = average string length
        # Space: O(k) building the string from result []
