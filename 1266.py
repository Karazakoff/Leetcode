class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        points.append(points[-1])
        sum = 0
        k = 0
        while k < len(points) - 2:
            x1, y1 = points[k]
            x2, y2 = points[k + 1]
            if x1 <= x2 and y1 <= y2:
                while x1 < x2 or y1 < y2:
                    if x1 < x2 and y1 < y2:
                        sum = sum + 1
                        x1 = x1 + 1
                        y1 = y1 + 1
                    elif x1 == x2:
                        y1 = y1 + 1
                        sum = sum + 1
                    elif y1 == y2:
                        x1 = x1 + 1
                        sum = sum + 1
            elif x1 <= x2 and y1 >= y2:
                while x1 < x2 or y1 > y2:
                    if x1 < x2 and y1 > y2:
                        sum = sum + 1
                        x1 = x1 + 1
                        y1 = y1 - 1
                    elif x1 == x2:
                        y1 = y1 - 1
                        sum = sum + 1
                    elif y1 == y2:
                        x1 = x1 + 1
                        sum = sum + 1
            elif x1 >= x2 and y1 >= y2:
                while x1 > x2 or y1 > y2:
                    if x1 > x2 and y1 > y2:
                        sum = sum + 1
                        x1 = x1 - 1
                        y1 = y1 - 1
                    elif x1 == x2:
                        y1 = y1 - 1
                        sum = sum + 1
                    elif y1 == y2:
                        x1 = x1 - 1
                        sum = sum + 1
            elif x1 >= x2 and y1 <= y2:
                while x1 > x2 or y1 < y2:
                    if x1 > x2 and y1 < y2:
                        sum = sum + 1
                        x1 = x1 - 1
                        y1 = y1 + 1
                    elif x1 == x2:
                        y1 = y1 + 1
                        sum = sum + 1
                    elif y1 == y2:
                        x1 = x1 - 1
                        sum = sum + 1

            k = k + 1
        return sum

Resh = Solution()
print(Resh.minTimeToVisitAllPoints([[3,2],[-2,2]]))
