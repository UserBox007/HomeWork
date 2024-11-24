from operator import truediv

numbers     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes      = []
not_primes  = []

range_ = range(1, len(numbers))

for i in range_:
    is_prime = True
    num1 = numbers[i]
    for j in range_:
        num2 = numbers[j]
        if (num1 != num2) & (num1 % num2 == 0):
            is_prime = False
    if is_prime:
        primes.append(num1)
    else:
        not_primes.append(num1)

print(primes)
print(not_primes)