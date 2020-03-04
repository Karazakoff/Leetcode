class Solution(object):
    def subtractProductAndSum(self, n):
        mult = 1
        sum = 0
        while n > 0:
            mult = mult * (n % 10)
            sum = sum + (n % 10)
            n = n // 10
        return mult - sum

Resh = Solution()
print(Resh.subtractProductAndSum(234))
