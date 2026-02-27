# Working with Lists
fruits = ["apple", "banana", "orange"]
print("Original list:", fruits)

# Access elements
print("First fruit:", fruits[0])

# Modify list
fruits.append("grape")
fruits.remove("banana")
print("Modified list:", fruits)


print("\n------------------\n")


# Working with Tuples
coordinates = (10, 20, 30)
print("Tuple:", coordinates)

# Access elements
print("First value:", coordinates[0])

# Try modifying tuple (will cause error if uncommented)
# coordinates[0] = 50   # Tuples are immutable


print("\n------------------\n")


# Working with Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Data Science"
}

print("Dictionary:", student)

# Access values using keys
print("Student name:", student["name"])

# Modify dictionary
student["age"] = 21
student["city"] = "Mumbai"

print("Updated dictionary:", student)