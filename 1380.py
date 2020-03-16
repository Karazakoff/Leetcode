class Solution(object):
    def luckyNumbers (self, matrix):
        minimum = min(matrix[0])
        maximum = max(matrix[0])
        result = minimum
        for i in range(1,len(matrix)):
            minimus = min(matrix[i])
            maximus = max(matrix[i])
            if minimus == maximus:
                return max(matrix)
            if minimum > maximus:
                result = minimum
            if minimus > maximum:
                result = minimus
            if maximum < maximus:
                maximum = maximus
        array = [result]
        return array




Resh = Solution()
print(Resh.luckyNumbers([[56216],[63251],[75772],[1945],[27014]]))
