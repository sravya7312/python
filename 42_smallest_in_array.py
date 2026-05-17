arr = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)