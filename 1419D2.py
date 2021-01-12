# contest: Codeforces Round #671 (Div. 2)
# problem: (D2) Sage's Birthday (hard version)

import math
 
def solution(n, a):
    a.sort()
    low = 0
    r1, r2 = math.ceil((n-2)/2), [0]*n
 
    for i in range(n):
        if i <= r1-1 and a[i] == a[i + n//2 + 1]:
            low += 1
        if i % 2:
            r2[i] = a[i//2]
        else:
            r2[i] = a[n//2 + i//2]
    
 
    return [r1 - low, r2]
 
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split(' '))) 
    x = solution(n, a)
    print(x[0])
    print(*x[1])