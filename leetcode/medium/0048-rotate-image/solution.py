class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,n):
            matrix[i].reverse()




        