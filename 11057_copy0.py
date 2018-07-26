#오르막수

N = int(input())


DP = [[1,1,1,1,1,1,1,1,1,1] for i in range(N)]

for i in range(N):
    for j in range(10):
        if i > 0:
            DP[i][0] = sum(DP[i-1])
            DP[i][j] = DP[i][j-1] - DP[i-1][j-1]
        else:
            pass
            

print(sum(DP[N-1])%10007)