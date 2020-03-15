class Solution(object):
    def removeOuterParentheses(self, S):
        array = []
        sum = 0
        finish = ""
        for i in S:
            if i == '(':
                sum = sum + 1
                array.append(i)
            elif i == ')':
                sum = sum - 1
                array.append(i)
            if sum == 0:
                finish = finish + "".join(array[1:len(array)-1])
                array = []
        return finish


Resh = Solution()
print(Resh.removeOuterParentheses("(()())(())(()(()))"))
