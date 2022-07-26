#week 6 solution

from itertools import permutations
def validity(words, result): #to validate the input and result
    d = {}
    val = list(set(result.join(words)))
    final = len(val)
    pos = permutations("0123456789", final) #creating possible combination
    if final > 10:
        return False
    else:
        for each in pos:
            for i in range(final): #assigning each character with possible value
                d[val[i]] = each[i]
            if check(d, words, result): 
                return True
                break
    return False

def check(d, word, rt): #function to calculate sum and validate with passed values
    word = words.copy()
    rt = result
    sm = 0
    for each in d:
        for i in range(len(word)):
            word[i] = word[i].replace(each, d[each])
        rt = rt.replace(each, d[each])
    for each in word:
        sm += int(each)
    if sm==int(rt):
        return True
    return False

words = [x for x in input().split()]
result = input()
print(validity(words,result))