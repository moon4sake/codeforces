#  contest: Codeforces Round #667 (Div. 3)
#  problem: (E) Two Platforms

def solution(n, k, x, y):
    x.sort()
    l, r, a, b, c = [], [], 0, 0, 1
    while b < n:
        if c <= n - 1:
            while x[c] - x[b] <= k:
                c += 1
                if c == n: break
 
        while x[b] - x[a] > k:
            a += 1
 
        r.append(c - b)
        l.append(b - a + 1)
        
        b += 1
        
    for i in range(1, n):
        l[i] = max(l[i - 1], l[i])
        r[n - 1 - i] = max(r[n - 1 - i], r[n - i])
 
    max_ = l[0]
    
    for i in range(n - 1):
        max_ = max(max_, l[i] + r[i + 1])
    
    return max_
    
if __name__ == "__main__":
    t = int(input())    
 
    for _ in range(t):
        n, k = map(int, input().split(' '))    
        x = list(map(int, input().split(' ')))
        y = list(map(int, input().split(' ')))
        print(solution(n, k, x, y))