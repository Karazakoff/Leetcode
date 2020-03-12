class Solution(object):
    def replaceElements(self, array):
        new_arr = []
        for i in range(len(array)):
            del array[0]
            new_arr.append(max(array))
        return new_arr









Resh = Solution()
print(Resh.replaceElements([17,18,5,4,6,1]))
