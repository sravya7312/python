arr = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = second = 999999

for i in arr:
    if i < smallest:
        second = smallest
        smallest = i
    elif i < second and i != smallest:
        second = i

print("Second smallest:", second)