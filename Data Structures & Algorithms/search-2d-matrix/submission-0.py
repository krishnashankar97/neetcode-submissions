class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        curr_row = -1
        for row in range(len(matrix)):
            if target <= matrix[row][-1]:
                curr_row = row
                break
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + ((r-l)//2)
            if matrix[curr_row][m] > target: r = m - 1
            elif matrix[curr_row][m] < target: l = m + 1
            else:
                return True
        return False