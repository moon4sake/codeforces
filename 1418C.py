# contest: Educational Codeforces Round 95 (Rated for Div. 2)
# problem: (C) Mortal Kombat Tower

def solution(n, a):
    if n == 1:  return a[0]
    
    # creating two dimensional list due to the time limit
    # time limit was strict in this round
    # especially for python, pypy, etc.
    dp = [[0, 0] for i in range(n)]
    dp[n-1], dp[n-2] = [a[n-1], 0], [a[n-2], 0]
    
    for i in range(n-3, -1, -1):
        dp[i][0] = min(a[i] + dp[i+1][1], a[i] + a[i+1] + dp[i+2][1])
        dp[i][1] = min(dp[i+1][0], dp[i+2][0])
 
    return dp[0][0]
 
 
if __name__ == "__main__":
    t = int(input())    
 
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solution(n, a))