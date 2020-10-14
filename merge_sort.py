def merge(A, p, q):
    if p < q:
        mid = (p+q)//2
        merge(A, p, mid)
        merge(A, mid+1, q)
        mergesort(A, p, q, mid)
    return A

def mergesort(A, p, q, mid):
    C = A[p: mid+1]
    D = A[mid+1:q+1]
    E = [0]*(len(A))
    i = 0
    c = 0
    d = 0
    while c < len(C) and d < len(D):
        if C[c] < D[d]:
            E[i] = C[c]
            c += 1
            
        else:
            E[i] = D[d]
            d += 1
        i += 1
        
    while c < len(C):
        E[i] = C[c]
        c += 1
        i += 1
    while d < len(D):
        E[i] = D[d]
        d += 1
        i += 1
    k = 0
    for i in range(p, q+1):
        A[i] = E[k]
        k += 1

A = [5, 4, 2, 1, 3]
merge(A, 0, 4)
print(A)


    
