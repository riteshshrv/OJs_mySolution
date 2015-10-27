'''You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]'''

def findSubstring(self, S, L):
        res = []            # result list
        num = len(L)        # length of the str list 
        ls = len(S)
        if num == 0:
            return []
        str_len = len(L[0]) 
        map_str = dict((x,L.count(x)) for x in set(L))
        i = 0
        while i + num * str_len - 1 < ls:
            map_str2 = {}
            j = 0
            while j < num:
                subs = S[i + j * str_len:i + j * str_len + str_len ]
                if not subs in map_str:
                    break
                else:
                    map_str2[subs] = map_str2.get(subs, 0) + 1
                    if map_str2[subs]>map_str[subs]:
                        break
                    j = j + 1
            if j == num:
                res.append(i)
            i = i + 1
         
        return res