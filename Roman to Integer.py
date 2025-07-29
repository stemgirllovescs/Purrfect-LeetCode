from typing_extensions import IntVar


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Convert Roman Symbol to Integer value
        # I             1
        # IV            4
        # V             5
        # IX            9
        # X             10
        # XL            40
        # L             50
        # XC            90
        # C             100
        # CD            400
        # D             500
        # CM            900
        # M             1000
        hashMap = {"I": 1, "IV" : 4, "V": 5, "IX" : 9, "X" : 10, "XL": 40, "L": 50,
        "XC" : 90, "C" : 100, "CD" : 400, "D" : 500, "CM" : 900, "M": 1000}

        result = 0
        # I want to go through the whole string s, then we either grab 1 or 2 chars,
        # depending on whether or not you can find them from the hashMap as valid symbols
        index = 0
        while index < len(s):
            # we either grab 1 or 2 chars when it's in the hashMap, 
            # then add that value to result
            if index + 1 < len(s) and s[index] + s[index + 1] in hashMap:
                result += hashMap[s[index] + s[index + 1]]
                index += 2
            else:
                result += hashMap[s[index]]
                index += 1
        return result


        # Runtime O(N) Space O(1) hashmap of 13 keys
        