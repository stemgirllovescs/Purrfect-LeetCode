class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep track of max number and currMax, when currMax < 0, reset to 0
        currMax = 0
        result = nums[0]

        for num in nums:
            if currMax < 0:
                currMax = 0
            currMax += num
            result = max(result, currMax)
        return result
        # Runtime O(N)
        # Space O(1)

