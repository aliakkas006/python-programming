num = int(input("Enter the upper limit for prime numbers: "))
prime = []

for i in range(num + 1):
    prime.append(i)

prime[0] = 0
prime[1] = 0

p = 2
while p * p <= num:
    if p != 0:
        for i in range(p * 2, num + 1, p):
            prime[i] = 0

    p += 1

print(f"All the prime numbers are up to {num}: ")

for i in range(len(prime)):
    if prime[i] != 0:
        print(prime[i], end=" ")


# prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
