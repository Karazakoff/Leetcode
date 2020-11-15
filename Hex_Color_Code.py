acceptable = ['#','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f']
answer = []
number = int(input())
for _ in range(number):
    line = input()
    if line != '':
        if line[0] == '#':
            continue
    pointer = False
    check = ""
    for i in line:
        if i == '#':
            pointer = True
        if i == ';' and check != "":
            pointer = False
            answer.append(check)
            check = ""
        if i == ',' and check != "":
            pointer = False
            answer.append(check)
            check = ""
        if i == ')' and check != "":
            pointer = False
            answer.append(check)
            check = ""
        if pointer == True:
            check += i
    # print("check = {}".format(check))
    # print("pointer =", pointer)
    # print("answer = {}".format(answer))
    if len(check) != 0:
        answer.append(check)

# print(answer)

for index, word in enumerate(answer):
    if len(word) > 7:
        continue
    elif len(word) < 4:
        continue
    for i in word:
        if i not in acceptable:
            break
    else:
        print(word)
