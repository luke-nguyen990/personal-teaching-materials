# https://codeforces.com/problemset/problem/116/A


num_stops = int(input())
ans = 0
cur_passengers = 0
while num_stops:
    num_exit, num_enter = map(int, input().split())
    cur_passengers += num_enter - num_exit
    ans = max(ans, cur_passengers)
    num_stops -= 1

print(ans)
