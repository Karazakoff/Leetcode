class Solution(object):
    def oddCells(self, n, m, indices):
        counter = 0
        sum = 0
        a = [[0 for x in range(m)] for y in range(n)]
        for index in indices:
            r, c = index
            if counter == len(indices):
                for i in range(m):
                    a[r][i] = a[r][i] + 1
                    if a[r][i] % 2 != 0:
                        sum = sum + 1

                for j in range(n):
                    a[j][c] = a[j][c] + 1
                    if a[j][c] % 2 != 0:
                        sum = sum + 1
            else:
                for i in range(m):
                    a[r][i] = a[r][i] + 1
                for j in range(n):
                    a[j][c] = a[j][c] + 1
                counter = counter + 1
        return counter

Resh = Solution()
print(Resh.oddCells(2,3,[[0,1],[1,1]]))
