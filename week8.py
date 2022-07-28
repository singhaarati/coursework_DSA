def findSteps(arr, keys, var):
    #assigning index value initially with 0
    i = 0
    j = 0
    steps = 0
    keysFound = ""
    while i<len(arr) and j<len(arr[0]): #iterating only if counter is less than n and m
        
        if len(keysFound) == keys: #if we find the desire number of keys we will return
            return steps-1
        if arr[i][j] == '@': #if '@' we just move to next step
            j += 1
            steps+=1
        elif arr[i][j] == '*':  #if '*' we move take another step
            if arr[i][j+1] in var.upper():
                j -= 1
                steps += 1
                continue
            steps += 1
            j += 1
        elif arr[i][j] in var: #when keys is found we add it to the keysFound 
            keysFound += arr[i][j]
            steps += 1
            j += 1
        elif arr[i][j] == '#': #if wall is encountered we move to another step
            i += 1
            steps+=1
        elif arr[i][j] in var.upper(): #if we encounter Lock and it is not necessary to open it
            j -= 1

var = "abcdefghijklmnopqrstuvwxyz"
arr = [
    ['@', '*', 'a', '*', '#'],
    ['#', '#', '#', '*', '#'],
    ['b', '*', 'A', '*', 'B']
]  
keys = 0
for item in arr:
    for element in item:
        if element in var:
            keys += 1



print(findSteps(arr,keys, var))