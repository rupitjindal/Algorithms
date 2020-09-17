def Fastest_Way(a,t,e,x,n):
    f = []
    l = []
    for i in range(2):
        f.append([])
        l.append([])
    f[0].append(e[0] + a[0][0])
    f[1].append(e[1] + a[1][0])
    for i in range(1,n):
        if (f[0][i-1]+a[0][i]) < (f[1][i-1] + t[1][i-1] + a[0][i]):
            f[0].append(f[0][i-1]+a[0][i])
            l[0].append(1)
        else:
            f[0].append(f[1][i-1]+a[0][i] + t[1][i-1])
            l[0].append(0)
            
        if f[1][i-1]+a[1][i] < f[0][i-1] + t[0][i-1] + a[1][i]:
            f[1].append(f[1][i-1]+a[1][i])
            l[1].append(0)
        else:
            f[1].append(f[0][i-1]+a[1][i] + t[0][i-1])
            l[1].append(1)
        print(f)
    if f[0][len(f[0])-1] + x[0] <= f[1][len(f[1])-1] +x[1]:
        f1 = f[0][len(f[0])-1] + x[0]
        l1 = 1
    else:
        f1 = f[1][len(f[0])-1] + x[1]
        l1 = 2
    return f1,l1
            

a = [[7,9,3,4,8,4],[8,5,6,4,5,7]] # time taken by each machine at given line
t = [[2,3,1,3,4],[2,1,2,2,1]] # time taken for changing line
e = [2,4] # time to give input at first machine
x = [3,2] # time to give output at last node
n = len(a[0]) # no of machines at any line 
print(Fastest_Way(a,t,e,x,n))
        
            
        

        
            
        
