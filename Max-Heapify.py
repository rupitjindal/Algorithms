# sorting heap from index specified by input
def Max_Heapify(A,i):
    l = 2*i
    r = l+1
    if l<len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r<len(A) and A[r] > A[largest]:
        largest = r
    if largest !=i:
        swap = A[i]
        A[i] = A[largest]
        A[largest] = swap
        Max_Heapify(A,largest)
    return A



A = [int(x) for x in input("Enter Array value with first element as 0 ").split()]
index = int(input("Enter the root  of subtree to be sorted  ")) #Enter the root value of subtree to give its proper position
print(Max_Heapify(A,index))
