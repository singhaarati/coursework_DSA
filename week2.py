#week 2 solution of week 2
def final(a,rem):
    prod = 1
    for each in a:
        prod *= each
    if prod in rem: #if the product is found in the provided array
        return True
    else:
        return False
    
l = int(input())
a = [int(x) for x in input().split()]

from itertools import permutations
ans = permutations(a,l) #generating all the possible combination
done = True
for each in ans:
    rem = a.copy()
    for item in each:
        rem.remove(item)
    if final(each, rem):
        done = False
        print(*each)
        break
if done:
    print("Requirement not met")
    