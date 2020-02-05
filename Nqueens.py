c=0
x=[-1 for i in range(8)]
def place(k,i):
    for j in range(1,k):
        if x[j]==i or abs(x[j]-i)==abs(j-k):
            return False
    return True
def Nqueens(k,n):
    global c
    for i in range(1,n+1):
        if place(k,i):
            x[k]=i
            if k==n:
                c+=1
            else:
                Nqueens(k+1,n)
Nqueens(1,8)
print(c)
