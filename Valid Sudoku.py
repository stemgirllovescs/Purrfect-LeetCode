class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Avoid duplicates for rows, cols, and 3x3 boxes
        # Make hashset
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                # check rows
                if value in rows[row]:
                    return False
                rows[row].add(value)
                # check cols
                if value in cols[col]:
                    return False
                cols[col].add(value)
                # check boxes
                index = (row // 3) * 3 + (col // 3)
                if value in boxes[index]:
                    return False
                boxes[index].add(value)
        return True

        # O(N^2) runtime
        # O(1) space

