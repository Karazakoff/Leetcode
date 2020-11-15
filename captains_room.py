family = int(input())
answer = input().split()
library = dict()
for i in set(answer):
    library[str(i)] = 0
for i in answer:
    library[i] += 1
print(list(library.keys())[list(library.values()).index(min(library.values()))])
