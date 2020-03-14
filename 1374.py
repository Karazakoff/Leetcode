class Solution(object):
    def generateTheString(self, n):
        str = ""
        if n % 2 == 0 or n == 1:
            for i in range(n - 1):
                str = str + 'a'
            str = str + 'b'
        else:
            for i in range(n - 2):
                str = str + 'a'
            str = str + "bc"
        return str




Resh = Solution()
print(Resh.generateTheString(31))
