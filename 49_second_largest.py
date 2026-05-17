arr = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second = -999999

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)