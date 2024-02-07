N = int(input())
result = "Berhasil" if N > 1 and not any(N % i == 0 for i in range(2, int(N**0.5) + 1)) else "Gagal"
print(result)
