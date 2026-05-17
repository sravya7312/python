arr = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0

for i in arr:
    total += i

avg = total / len(arr)

print("Average:", avg)