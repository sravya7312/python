num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit ** 3
    num //= 10

if temp == sum_digits:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")