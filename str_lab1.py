print("Сизов Константин Васильевич, РПИб-о23")
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
i = 2
k = 0
if n % i:
    j = 3
    while j*j < n+1:
        if not n%j:
            k = 1
            i = j
            break
        j += 2
else:
    k = 1
if k:
    with open('output.txt', 'w') as f:
        f.write(f'{(i-1)*(n//i)} {n//i}\n')
else :
    with open('output.txt', 'w') as f:
        f.write(f'{(1)} {n-1}\n')

