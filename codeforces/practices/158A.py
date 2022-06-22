import bisect


n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
target = max(1, A[n - k])
print(n - bisect.bisect_left(A, target))
