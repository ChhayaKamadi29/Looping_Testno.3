#Write a program to calculate the sum of following series where n is input by user. 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

n = int(input("Enter the value of N: "))

total_sum = 0.0
fact = 1

for i in range(1, n + 1):
    fact *= i
    total_sum += i / fact

print(f"Sum of the series: {total_sum}")