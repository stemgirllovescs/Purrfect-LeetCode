class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Break, repaint, connect
        # Adjacent means checking both left and right
        # We will have a count variable, an array that stores colors, and 
        # a result array that stores the count variable
        count = 0
        array = [0] * n
        result = []

        # Go through the whole queries array
        for index, color in queries:
            # break old adjacent connections, check left and right, decrement count
                # if current element has a color
            if array[index] != 0:
                # check left and right and in bounds
                if index != 0 and array[index] == array[index - 1]:
                    count -= 1
                if index + 1 <= n - 1 and array[index] == array[index + 1]:
                    count -= 1

            # repaint the color of current element
            array[index] = color

            # build new adjacement connections, check left and right
            if array[index] != 0:
                # check left and right and in bounds
                if index != 0 and array[index] == array[index - 1]:
                    count += 1
                if index + 1 <= n - 1 and array[index] == array[index + 1]:
                    count += 1

            result.append(count)
        
        return result

        # Time Complexity: O(m)   m = query
        # Space Complexity: O(n + m)   n = color array and m = output list