from math import *
def Bucketsort(A):
    B= []
    for i in range(len(A)):
        B.append([])
    n = len(A)
    for i in range(0,n): #creating buckets of elements
        j = floor(n*A[i])
        B[j].append(A[i])
    for i in range(0,n): #aranging the elements sof buckets using insertion sort 
        insertionSort(B[i])
    for i in range(1,len(B)): #appening the sorted arrays to make a single array
        B[0]+=B[i]
    return B[0] #returning the sorted array

def insertionSort(A): #Sorting the subarray
    print(A)
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i-=1
        A[i+1] = key
    print(A)
    return A    
         
        
        
A = [ int(x) for x in input("Enter array to be sorted").split()]
print(Bucketsort(A))
