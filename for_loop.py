n = int(input('Enter any +ve integer : '))
a = n // 2
print(a)
for i in range(2, a):
    if n % i == 0:
        print(False)
    else:
        print(True)