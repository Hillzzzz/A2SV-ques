class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        numrow = len(matrix)
        numcol = len(matrix[0])
        for i in range(numrow - 1):
            for j in range(numcol - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
