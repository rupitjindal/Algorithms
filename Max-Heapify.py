#Building Heap and sorting it
def Build_Max_Heap(A):
    heap_size = len(A)
    for i in range(int((len(A)-1)/2),0,-1):
        print(i)
        Max_Heapify(A,i)
    return A
# Sorting heap
def Max_Heapify(A,i):
    l = 2*i
    r = l+1
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap = A[i]
        A[i] = A[largest]
        A[largest] = swap
        Max_Heapify(A,largest)
    return A
#Ener array
A = [int(x) for x in input("Enter Array value with first element as 0 ").split()]    
print(Build_Max_Heap(A))


