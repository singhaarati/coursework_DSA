#week 5 solution
def max_match(t,l): #function which returns maximum match of target word and words in given array
    d = {}
    s = ""
    for word in l:
        cnt = 0
        for each in t:
            if each in word:
                s += each
        d[word] = s #storing each word and its corresponding matched characters of target string
        s = ""
    maxMatch = max(d.values()) #finding maxmimum matched substring
    for key in d:
        if d[key]==maxMatch:
            return key,maxMatch #returning corresponding word of a array and maximum matched substring of a target string

A = [x for x in input().split()] #input of array of words
target = list(input()) #input of target word

cnt = 0 #count the number of word required from given array to form a targeted word
while len(A)>0 and len(target)>0:#finding max substr and its corresponding word of array untill one of them is empty
    try:
        cnt += 1
        key, val = max_match(target, A)
        A.remove(key)
        for each in val:
            target.remove(each)
    except:
        print("Target word cannot be formed with subset of given array of words") #if target word cannot be formed with subset of given array
        cnt =""
        break
print(cnt)