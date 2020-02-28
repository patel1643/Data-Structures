def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark



def mo3_quickSort(alist):
    mo3_quickSortHelper(alist,0,len(alist)-1)

def mo3_quickSortHelper(alist,first,last):
    
    if first<last:

        splitpoint = mo3_partition(alist,first,last)

        mo3_quickSortHelper(alist,first,splitpoint-1)
        mo3_quickSortHelper(alist,splitpoint+1,last)


def insertionSort(alist):
    for i in range(1,len(alist)):
        currVal = alist[i]
        pos = i
        while pos>0 and currVal<alist[pos-1]:
            alist[pos]=alist[pos-1]
            pos = pos-1
        alist[pos] = currVal
    return alist

def mo3_partition(alist,first,last):
    middle = (last-first)//2 +first
    median = [alist[first], alist[middle], alist[last]]
    median = insertionSort(median)

    pivotvalue = median[1]

    if (pivotvalue == alist[middle]):
        alist[first], alist[middle] = alist[middle], alist[first]
    elif (pivotvalue == alist[last]):
        alist[first], alist[last] = alist[last], alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark



