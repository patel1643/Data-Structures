import random
import pythonds

lsize = []
quickSortTime = []
mo3Time = []


def quickSort(alist):
    quickSortA(alist,0,len(alist)-1)

def quickSortA(alist,first,last):
    if first<last:
        midpoint = partition(alist,first,last)
        quickSortA(alist,first,midpoint-1)
        quickSortA(alist,midpoint+1,last)


def partition(alist,first,last):
    pivotValue = alist[first]

    leftPoint = first+1
    rightPoint = last

    done = False
    while not done:

        while leftPoint <= rightPoint and alist[leftPoint] <= pivotValue:
            leftPoint = leftPoint + 1

        while alist[rightPoint] >= pivotValue and rightPoint >= leftPoint:
            rightPoint = rightPoint -1

        if rightPoint < leftPoint:
            done = True
        else:
            temp = alist[leftPoint]
            alist[leftPoint] = alist[rightPoint]
            alist[rightPoint] = temp

    temp = alist[first]
    alist[first] = alist[rightPoint]
    alist[rightPoint] = temp


    return rightPoint



def mo3_quickSort(alist):
    mo3_quickSortA(alist,0,len(alist)-1)

def mo3_quickSortA(alist,first,last):

    if first<last:

        midpoint = mo3_partition(alist,first,last)

        mo3_quickSortA(alist,first,midpoint-1)
        mo3_quickSortA(alist,midpoint+1,last)


def insertionSort(alist):
    for i in range(1,len(alist)):
        current = alist[i]
        position = i
        while position>0 and current<alist[position-1]:
            alist[position]=alist[position-1]
            position = position-1
        alist[position] = current
    return alist

def mo3_partition(alist,first,last):
    middle = (last-first)//2 +first
    median = [alist[first], alist[middle], alist[last]]
    median = insertionSort(median)

    pivotValue = median[1]

    if (pivotValue == alist[middle]):
        alist[first], alist[middle] = alist[middle], alist[first]
    elif (pivotValue == alist[last]):
        alist[first], alist[last] = alist[last], alist[first]

    leftPoint = first+1
    rightPoint = last

    done = False
    while not done:

        while leftPoint <= rightPoint and alist[leftPoint] <= pivotValue:
            leftPoint = leftPoint + 1

        while alist[rightPoint] >= pivotValue and rightPoint >= leftPoint:
            rightPoint = rightPoint -1

        if rightPoint < leftPoint:
            done = True
        else:
            temp = alist[leftPoint]
            alist[leftPoint] = alist[rightPoint]
            alist[rightPoint] = temp

    temp = alist[first]
    alist[first] = alist[rightPoint]
    alist[rightPoint] = temp


    return rightPoint

