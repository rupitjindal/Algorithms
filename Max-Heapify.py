#Sorting Heap
def Heapsort(A):
    Build_Max_Heap(A)
    a = len(A)
    for i in range(a-1,1,-1):
            swap = A[1]
            A[1] = A[i]
            A[i] = swap
            Max_Heapify(A,1,i)
    return A

#Building Heap
def Build_Max_Heap(A):
        for i in range(int(((len(A)-1)/2)),0,-1):
            Max_Heapify(A,i,len(A))
        return A
#Maintaining Heap-Max property
def Max_Heapify(A,i,a):
    l = 2*i
    r = l+1
    if l< a and A[l] > A[i]:
        largest =  l
    else:
        largest = i
    if r<a and A[r] > A[largest]:
        largest = r
    if largest!= i:
        swap = A[i]
        A[i] = A[largest]
        A[largest] = swap
        Max_Heapify(A,largest,a)
    return A

A  = [int(x) for x in input("Enter array to be sorted starting with 0 ").split()]
print(Heapsort(A))
