# Day 1 - Part 2: Lists and Loops

# 1. Create a list of fruits
fruits = ["apple", "banana", "mango", "orange"]

# 2. Print the entire list
print("Fruits list:", fruits)

# 3. Print each fruit one by one using a loop
print("\nPrinting each fruit:")
for fruit in fruits:
    print(fruit)

# 4. Add a new fruit to the list
fruits.append("grape")
print("\nAfter adding grape:", fruits)

# 5. Remove one fruit
fruits.remove("banana")
print("\nAfter removing banana:", fruits)

# 6. Count how many fruits are left
print("\nTotal fruits:", len(fruits))
