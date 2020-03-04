class Solution(object):
    def numJewelsInStones(self, J, S):
        sum = 0
        for i in J:
            for j in S:
                if i == j:
                    sum = sum + 1
        return sum



Resh = Solution()
print(Resh.numJewelsInStones("aA", "aAAbbbbb"))
