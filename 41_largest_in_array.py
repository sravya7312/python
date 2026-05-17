arr = list(map(int, input("Enter numbers separated by space: ").split()))

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest element:", largest)