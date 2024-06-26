# 스타트와 링크

def dfs(n,alst,blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += capa[alst[i]][alst[j]]
                    bsm += capa[blst[i]][blst[j]]
            ans = min(ans, abs(asm-bsm))
        return
    
    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])

N = int(input())
M = N//2
capa = [list(map(int,input().split())) for _ in range(N)]
ans = 10000
dfs(0,[],[])
print(ans)


