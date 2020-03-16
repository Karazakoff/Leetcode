class Solution(object):
    def freqAlphabets(self, s):
        result = ""
        library = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i',
            '10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q',
            '18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        check = False
        s = s + "**"
        for i in range(len(s) - 2):
            if check:
                check = False
                continue
            if s[i] != '#':
                if int(s[i]) < 3 and s[i] != '0':
                    if s[i + 2] != '#':
                        result = result + library[s[i]]
                    else:
                        result = result + library[s[i:i+3]]
                        check = True
                else:
                    result = result + library[s[i]]
        return result





Resh = Solution()
print(Resh.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
