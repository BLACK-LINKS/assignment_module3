def sum_of_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum

num = int(input("Enter a number: "))
print("Sum of divisors of", num, "is", sum_of_divisors(num))
