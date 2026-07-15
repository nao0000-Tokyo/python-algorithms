# Prime Number Counter
This is a simple Python program that counts the number of prime numbers from **1** to **N**.
The program checks each integer by counting its divisors. If an integer has exactly **two divisors**, it is considered a prime number.
**Algorithm:** Brute Force
**Time Complexity:** `O(N²)`


N = int(input())

count = 0

for i in range(2, N + 1):
    divisor_count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            divisor_count += 1

    if divisor_count == 2:
        count += 1

print(count)