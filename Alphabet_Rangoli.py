alphabet = "abcdefghijklmnopqrstuvwxyz"
number = int(input())
alphabet = alphabet[:number]
till = (number - 1) * 4
mid = till // 2
counter = -2
for i in range(number):
    for j in range(mid):
        print('-', end = "")
    new_alphabet = alphabet[-1:counter:-1]
    for k in new_alphabet:
        if k == new_alphabet[-1]:
            break
        print(k, end = '')
        print('-', end = '')
    new_second_alphabet = alphabet[-1:counter:-1]
    # print("\nnew_second_alphabet = ",new_second_alphabet)
    for k in reversed(new_second_alphabet):
        print(k, end = '')
        if k == new_second_alphabet[0]:
            break
        print('-', end = '')
    for j in range(mid):
        print('-', end = "")
    mid = mid - 2
    counter = counter - 1
    print()
second_alphabet = alphabet[1:]
# ------------------------------------------------------------------------------------
# print("mid = ", mid)
# print("counter = ", counter)
# print("alphabet = ", alphabet)
# print("second_alphabet = ", second_alphabet)
# ------------------------------------------------------------------------------------
counter = 1
mid = 2
for i in range(number - 1):
    for j in range(mid):
        print('-', end = '')
    new_alphabet = alphabet[counter:]
    # print("\n new_alphabet = ", new_alphabet)
    for k in reversed(new_alphabet):
        print(k, end = '')
        if k == new_alphabet[0]:
            break
        print('-', end = '')
    new_second_alphabet = alphabet[counter + 1:]
    for k in new_second_alphabet:
        print('-', end = '')
        print(k, end = '')
    for j in range(mid):
        print('-', end = '')

    counter = counter + 1
    mid = mid + 2
    print()
