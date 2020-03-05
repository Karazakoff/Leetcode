class Solution(object):
    def findNumbers(self, nums):
        s = 0
        for i in nums:
            i = str(i)
            if len(i) % 2 == 0:
                s = s + 1
        return s


Resh = Solution()
nums = [12,345,2,6,7896]
print(Resh.findNumbers(nums))
