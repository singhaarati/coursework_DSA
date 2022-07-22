#Solution of week 4
villageGrades = [int(x) for x in input("Enter Village Grades: ").split()] #Taking input of village grades
villageGrades.sort() 

PreviousVillage = villageGrades[0] #village with lowest grade will always recieve least number of containers i.e., 1
TotalContainers = 1 
ContainerCount = 1 


for i in range(1,len(villageGrades)): 
    if villageGrades[i] > PreviousVillage:
        #if village has higher grade than previous Village it will recieve higher number of containers
        ContainerCount += 1
        TotalContainers += ContainerCount
    else:
        #if village has same grade as previous village it will recieve same number of containers
        TotalContainers += ContainerCount
    PreviousVillage = villageGrades[i] 
print(TotalContainers)
