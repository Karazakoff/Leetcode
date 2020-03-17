class Solution(object):
    def distributeCandies(self, candies, num_people):
        pluser = 0 - num_people
        array = [0] * (num_people + 1)
        while candies > 0:
            pluser = pluser + num_people
            for i in range(1,num_people + 1):
                if i + pluser < candies:
                    array[i] = array[i] + i + pluser
                    candies = candies - i - pluser
                else:
                    array[i] = array[i] + candies
                    return array[1:num_people + 1]



Resh = Solution()
print(Resh.distributeCandies(20,4))
