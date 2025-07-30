class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # A helper method to reverse start and end
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # set k as k % len of array nums to make sure we don't go out of bounds
        k = k % len(nums)
        # reverse the whole thing
        reverse(0, len(nums) - 1)
        # reverse first half from 0 to k - 1 because of 0 index
        reverse(0, k - 1)
        # reverse second half, from k to end of array
        reverse(k, len(nums) - 1)
        
        #O(N) runtime
        #O(1) space