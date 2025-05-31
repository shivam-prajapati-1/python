
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]


print("Original list of fruits:", fruits)


fruits.append("Pineapple")
print("After adding 'Pineapple':", fruits)


fruits.remove("Banana")
print("After removing 'Banana':", fruits)


fruits.sort()
print("After sorting:", fruits)


print("\nList of fruits:")
for fruit in fruits:
    print(fruit)
