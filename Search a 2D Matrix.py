class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # You need to flatten the 2D array 
        # Binary Search where row and col are determined by mid // n or mid % n
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            # now we move pointers when necessary
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left += 1
            elif matrix[row][col] > target:
                right -= 1
        return False
        # runtime O(log M * N) because of binary search
        # space O(1)