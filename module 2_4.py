
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
leng = len(numbers)
primes = []
not_primes = []

for i in range (2, leng):
    for j in range (2, (i//2) + 1):
        if i % j == 0:
           not_primes.append(i)
           break
    if i not in not_primes:
       primes.append(i)

print(primes)
print(not_primes)
