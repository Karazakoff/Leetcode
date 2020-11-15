vowels = ['A','E','I','O','U']

banan = input()
zalkar = 0
yunus = 0
for i in range(len(banan)):
    if banan[i] in vowels:
        yunus += len(banan[i:])
    else:
        zalkar += len(banan[i:])
if yunus <= zalkar:
    print("Stuart {}".format(zalkar))
else:
    print("Kevin {}".format(yunus))
