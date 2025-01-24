n,m = map(int, input().split())

matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]


result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(m)] for i in range(n)]

for row in result:
    print(*row)