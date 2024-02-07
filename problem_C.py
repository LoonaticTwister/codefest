n = int(input('Jumlah anime : '))
m = int(input('Jumlah waktu : '))
x = []
c = 0
for a in range(n):
    a = int(input('waktu : '))
    x.append(a)
x.sort()
for i in x:
    if m >= i:
        c += 1
        m -= i
    else:
        break
print(c)