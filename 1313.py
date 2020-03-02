class Solution(object):
    def decompressRLElist(self, nums):
        array = []
        for i in range(0,len(nums) // 2):
            for j in range(0,nums[i * 2]):
                array.append(nums[i * 2 + 1])
        return array


Resh = Solution()
print(Resh.decompressRLElist([1,2,3,4]))
