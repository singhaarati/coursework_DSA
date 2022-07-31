#solution of week 1
#linked List code
import numpy as np
class NODE():
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, new_node):
        self.nextNode = new_node

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def Add(self, data):
        new_node = NODE(data)
        new_node.setNext(self.head)
        self.head = new_node

def Merge(L1, L2):
    temp = None
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.data <= L2.data:
        temp = L1
        temp.nextNode = Merge(L1.nextNode, L2)
    else:
        temp = L2
        temp.nextNode = Merge(L1, L2.nextNode)
    return temp

def sortAndGetMedian(L1):
    SortedList = []
    CurrentNode = L1.head
    while CurrentNode != None:
        SortedList.append(CurrentNode.getData())
        CurrentNode = CurrentNode.getNext()
        
    SortedList.sort()
    print("Sorted elements of Linked list: ", *SortedList)
    
    #By using numpy, finding median
    MedianUsingNumpy = np.median(SortedList)
    print("Median of the Merged List using Numpy: ", MedianUsingNumpy)

    #By using formula, finding median
    midValue = len(SortedList) // 2
    median = (SortedList[midValue] + SortedList[~midValue]) / 2
    print("Median of the Merged List using Formula: ", median)
    
k = int(input("number of linked list: ")) #Taking input for number of the kth linked list
mergeLinkedList = LinkedList() #initializing the final LinkedList Linked Merged List

for i in range(k):
    n = int(input(f"Enter number of elements in {i+1} linked list: ")) 
    li = LinkedList()
    for j in range(n):
        li.Add(int(input(f"Enter {j+1} element: "))) 
    
    mergeLinkedList.head = Merge(mergeLinkedList.head, li.head) #Linked List merging
    
sortAndGetMedian(mergeLinkedList) #function calling to get median of mergedLinkList