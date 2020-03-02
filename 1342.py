class Solution(object):
    def numberOfSteps (self, num):
        if num == 0:
            return
        elif num % 2 == 0:
            return numberOfSteps(num // 2) + 1
        elif num % 2 != 0:
            return numberOfSteps(num - 1) + 1

Result = Solution()
Result.numberOfSteps(17)
