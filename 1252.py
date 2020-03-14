class Solution(object):
    def oddCells(self, n, m, indices):

        sum = 0
        a = [[0 for x in range(m)] for y in range(n)]


        for index in indices:
            r, c = index
            for i in range(m):
                a[r][i] = a[r][i] + 1
            for j in range(n):
                a[j][c] = a[j][c] + 1

        for i in range(n):
            for j in range(m):
                if a[i][j] % 2 != 0:
                    sum = sum + 1
        return sum

Resh = Solution()
print(Resh.oddCells(2,3,[[0,1],[1,1]]))
