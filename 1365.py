def smallerNumbersThanCurrent(self, nums):
    mas = []
    for i in range(0,len(nums)):
        sum = 0
        for j in range(0,len(nums)):
            if nums[j] < nums[i]:
                sum = sum + 1
        mas.append(sum)
    return mas


print(smallerNumbersThanCurrent(1,[4,1,2,3]))
