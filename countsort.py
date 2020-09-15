def  Countsort(A,k):
    C = []
    B = []
    for i in range(0,k+1): #creating a subarray and initializing it
        C.append(0)
    for i in range(1,len(A)+1): #creating output array and initializing it
         B.append(0)
    for i in range(1,len(A)): #giving the position of numbers and finding the number of times occurence of an element
        C[A[i]] = C[A[i]] + 1
    for i in range(1,len(C)): # finding total elements smaller than a particular element
        C[i] = C[i] + C[i-1]
    for i in range(1,len(A)): # creating output array
        B[C[A[i]]] = A[i]
        C[A[i]]-=1
    return B

A = [int(x) for x in input("Enter array to be sorted ").split()]
x = int(input("Enter maximum element in the array "))
print("Your sorted ARRAY is ",Countsort(A,x))


    
