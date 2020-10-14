def DFS(M, nV):
    visit = [0]*nV
    stack = []
    for i in range(nV):
        if visit[i] == 0:
            DFS_recur(M, i, stack, nV, visit)



def DFS_recur(M, u, stack, nV, visit):
    stack.append(u)
    visit[u] = 1
    for j in range(nV):
        if M[u][j] == 1 and visit[j] == 0:
            DFS_recur(M, j, stack,nV, visit)
    print(stack.pop())


M = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1],[0, 0, 1, 0, 0],[0,0, 1, 0, 0]]
print("\n", M)
DFS(M, 5)
