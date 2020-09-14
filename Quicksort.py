def Quicksort(A,p,r): 
    if p<r:
        q = Partition(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)
    return A

def Partition(A,p,r): #divides the array into subarrays
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<A[r]:
            i+=1
            swap = A[i]
            A[i] = A[j]
            A[j] = swap
    swap = A[r]
    A[r] = A[i+1]
    A[i+1] = swap
    return i+1

A= [for x in input("Enter array to be sorted ").split()]
print(Quicksort(A,0,len(A))) #Here starting point in by default zero but user can select any other starting point
