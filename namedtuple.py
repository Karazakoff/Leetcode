from collections import namedtuple
n = int(input())
scores = []
Score = namedtuple('Score', input().split())
for i in range(n):
    scores.append(Score(*input().split()).MARKS)
print("%.2f"% (sum(map(int,scores))/n))
