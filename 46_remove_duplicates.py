arr = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print("Array after removing duplicates:", unique)