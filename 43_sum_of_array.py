arr = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0

for i in arr:
    total += i

print("Sum of array:", total)