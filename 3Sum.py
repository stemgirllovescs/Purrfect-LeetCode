class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Sort the array
        # aaabbbbcccc
        # Two pointers, skip duplicated values
        nums.sort()
        result = []

        for index, value in enumerate(nums):
            # skip the duplicated values of the first value
            if (index != 0 and nums[index] == nums[index - 1]):
                continue
            
            # two pointers
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = value + nums[left] + nums[right]
                if total == 0:
                    # we found a triplet! append it to result
                    result.append([value, nums[left], nums[right]])

                    # skip duplicated value of second and or third value
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
        # Runtime O(N^2)
        # Space O(N)