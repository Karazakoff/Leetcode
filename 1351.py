class Solution(object):
    def countNegatives(self, grid):
        sum = 0
        for gri in grid:
            for i in gri:
                if i < 0:
                    sum = sum + 1
        return sum

Resh = Solution()
print(Resh.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
