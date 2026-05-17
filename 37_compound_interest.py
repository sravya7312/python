p = float(input("Enter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

ci = p * (1 + r / 100) ** t - p

print("Compound Interest:", ci)