
num = int(input("Enter a number to print its multiplication table: "))


i = 1


print(f"\nMultiplication Table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
