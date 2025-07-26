class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort by the starting point in ascending order
        intervals.sort(key = lambda x: x[0])

        # Store the first interval in the result array, there is no other to compare
        result = [intervals[0]]

        # Go through the intervals
        for start, end in intervals:
            previousEnd = result[-1][-1]
            # if current start is <= previousEnd, there is an overlap
            if start <= previousEnd:
                result[-1][-1] = max(previousEnd, end)
            else: # no overlap
                result.append([start, end])
        return result
        # O(N log(N)) runtime because of sorting
        # O(N) space because of result array