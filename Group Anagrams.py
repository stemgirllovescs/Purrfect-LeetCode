from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        # hashmap of string : list of strings
        # sorted string : list of original unsorted strings
        hashMap = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            hashMap[key].append(str)
        
        return list(hashMap.values())

        # runtime O(N · k log k), n = length of strs, k = max length of a str in strs
        # space O(N * k)