N = int(input())
MOD = 10**9 + 7
a, b = 1, 1

for _ in range(2, N + 1):
    a, b = b, (a + b) % MOD

print(b)
