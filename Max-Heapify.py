def Build_Max_Heap(A): #Build Heap of given array
    a = len(A)
    for i in range(int(a/2),0,-1):
        Max_Heapify(A,i)
    return A

def Max_Heapify(A,i): #Maintains heap property
    l =2*i
    r = l+1
    if  l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if  r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap = A[i]
        A[i] = A[largest]
        A[largest] = swap
        Max_Heapify(A,largest)
    return A
        
def Heap_Maximum(A): #Gives Maximum element of heap
    return A[1]

def Heap_Max_Extract(A): #Extract Maximum element of heap
    Build_Max_Heap(A)
    if len(A) < 1:
        print("HEAP UNDERFLOW!!!...")
    else:
        maxE = A[1]
        a = len(A)
        A[1] = A[a-1]
        a-=1
        Max_Heapify(A,1)
        return maxE

def Max_Heap_Key(A,i,key): #Raised key of an element of heap
    Build_Max_Heap(A)
    if key < A[i]:
        print("NEW KEY IS SMALLER THAN CURRENT KEY")
    else:
        A[i] = key
        while(i>1 and A[Parent(i)]< A[i]):
            swap = A[Parent(i)]
            A[Parent(i)] = A[i]
            A[i] = swap
            i = Parent(i)
    return A

def Parent(i): #gives Parent of heap
    return int(i/2)

def Max_Heap_Insert(A,key):
    Build_Max_Heap(A)
    A.append(-3.2e10)
    a = len(A)-1
    Max_Heap_Key(A,a-1,key)
    A.pop()
    return A

A = [int(x) for x in input("Enter Array to be converted into heap starting with 0 ").split()]
index , key = [int(x) for x in input("Enter element's index and its raised key ").split()]
insert = int(input("Enter Element to be inserted"))

print("Heap build", Build_Max_Heap(A))
print( Max_Heap_Key(A,index,key))
print(Max_Heap_Insert(A,insert))
print( Heap_Max_Extract(A))

       
