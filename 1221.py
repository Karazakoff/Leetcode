class Solution(object):
    def balancedStringSplit(self, s):
        checker = 0
        sum = 0
        for i in s:
            if i == 'R':
                checker = checker + 1
            elif i == 'L':
                checker = checker - 1
            if checker == 0:
                sum = sum + 1
        return sum


Resh = Solution()
print(Resh.balancedStringSplit(1, "RRLLRRLLLLRRR"))
