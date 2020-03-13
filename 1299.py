class Solution(object):
    def replaceElements(self, arr):
        new_arr = []
        for i in range(len(arr) - 1):
            new = arr[i + 1:]
            new_arr.append(max(new))
        new_arr.append(-1)
        return new_arr


Resh = Solution()
print(Resh.replaceElements([17,18,5,4,6,1]))
