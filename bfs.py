def bfs(M, s, nV):
    visit = [0]*nV
    q = []
    q.append(s-1)
    visit[s-1] = 1
    while q:
        s = q[0]+1
        for j in range(nV):
            if M[s-1][j] == 1 and visit[j] == 0:
                q.append(j)
                visit[j] = 1
        print(q.pop(0)+1)

M = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1],[0, 0, 1, 0, 0],[0,0, 1, 0, 0]]
print("\n", M)
print("When graph is in matrix")
bfs(M, 1, 5)

def bfs_list(A, s, nV):
    s -= 1
    visit = [0]*nV
    q = []
    q.append(s)
    visit[s] = 1
    while q:
        s = q[0]
        for j in A[s]:
            if visit[j] == 0:
                q.append(j)
                visit[j] = 1
        print(q.pop(0)+1)

A = {0:[1], 1:[0, 2], 2:[1, 3, 4], 3:[2], 4:[2]}
print("\n", A)
print("When graph is in List")
bfs_list(A,1,5)
    
        
    
    
