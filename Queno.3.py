#Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp and also total salary of all emp.

n = int(input("Enter the number of emp: "))

total =0

for i in range(1, n + 1):
    print(f"\n--Employee {i}--")
    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total_salary = basic + da + ta + hra
    total += total_salary

    print(f"Allowances DA: {da}, TA: {ta}, HRA: {hra}")
    print(f"Total Salary of Employee {i}: {total_salary}")

print(f"\nTotal salary of all {n} employees: {total}")