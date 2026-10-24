class Solution:
    def rotateMatrix(self, mat):
        n=len(mat)
        for i in range(0,n-1):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for i in range(0,n):
            mat.reverse()
            return mat
        