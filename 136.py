class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        check = 10
        for i in range(len(nums)-1):
            if nums[i] != nums[i + 1] and nums[i] != check:
                return nums[i]
            else:
                check = nums[i]
        return nums[-1]


Resh = Solution()
print(Resh.singleNumber([2,2,1]))
