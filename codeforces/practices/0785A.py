# https://codeforces.com/problemset/problem/785/A


polyhedrons_map = dict()
polyhedrons_map['Tetrahedron'] = 4
polyhedrons_map['Cube'] = 6
polyhedrons_map['Octahedron'] = 8
polyhedrons_map['Dodecahedron'] = 12
polyhedrons_map['Icosahedron'] = 20

case = int(input())
ans = 0
for c in range(case):
    ans += polyhedrons_map[input()]

print(ans)
