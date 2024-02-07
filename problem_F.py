n = int(input('Masukkan sebuah angka: '))
x = ''
for a in range(n):
    if (a) % 2 == 0:
        x = '1' + x
    elif (a) % 2 != 0:
        x = '0' + x
    print(x)