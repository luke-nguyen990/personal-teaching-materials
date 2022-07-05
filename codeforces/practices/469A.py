# https://codeforces.com/problemset/problem/469/A


levels = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = set(A[1:])
B = set(B[1:])

if levels == len(A.union(B)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
