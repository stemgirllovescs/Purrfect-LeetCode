from unicodedata import digit


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # [9, 1, 4] = [9, 1, 5]
        # [9, 9, 9] = [1, 0, 0 , 0]
        # loop from reverse
        for index in range(len(digits) -1, -1, -1):
            # if current val is not 9, then we increment the value by 1
            # return early for digits
            if digits[index] != 9:
                digits[index] += 1
                return digits
            else:
            # else it's 9, so we turn it into a 0
                digits[index] = 0
        # return [1] + rest of the digits array
        return [1] + digits
        # O(N) for runtime
        # O(1) for space
