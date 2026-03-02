"""
Practice Exercises: Loops and Iteration
========================================
Complete these exercises to reinforce your understanding of loops.
"""

print("PRACTICE EXERCISES - LOOPS AND ITERATION")
print("=" * 60)

# =============================================================================
# EXERCISE 1: FOR LOOP - Sum of Numbers
# =============================================================================
print("\n📝 EXERCISE 1: Calculate sum of numbers 1 to 10")
print("-" * 60)

# Your solution here:
total = 0
for num in range(1, 11):
    total += num
print(f"Sum of numbers 1 to 10: {total}")

# =============================================================================
# EXERCISE 2: FOR LOOP - Count Even Numbers
# =============================================================================
print("\n📝 EXERCISE 2: Count even numbers in a list")
print("-" * 60)

numbers = [12, 7, 23, 18, 5, 14, 9, 20]
print(f"Numbers: {numbers}")

# Your solution here:
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(f"Count of even numbers: {even_count}")

# =============================================================================
# EXERCISE 3: WHILE LOOP - Find First Multiple
# =============================================================================
print("\n📝 EXERCISE 3: Find first number divisible by 7 starting from 50")
print("-" * 60)

# Your solution here:
num = 50
while num % 7 != 0:
    num += 1
print(f"First number divisible by 7: {num}")

# =============================================================================
# EXERCISE 4: FOR LOOP WITH BREAK - Search
# =============================================================================
print("\n📝 EXERCISE 4: Find position of target value")
print("-" * 60)

data = [10, 25, 30, 45, 50, 60, 75]
target = 45
print(f"Data: {data}")
print(f"Target: {target}")

# Your solution here:
position = -1
for i in range(len(data)):
    if data[i] == target:
        position = i
        break
if position != -1:
    print(f"Target found at index: {position}")
else:
    print("Target not found")

# =============================================================================
# EXERCISE 5: FOR LOOP WITH CONTINUE - Filter Data
# =============================================================================
print("\n📝 EXERCISE 5: Filter and sum positive numbers only")
print("-" * 60)

values = [10, -5, 20, -3, 15, -8, 25]
print(f"Values: {values}")

# Your solution here:
positive_sum = 0
for val in values:
    if val < 0:
        continue
    positive_sum += val
print(f"Sum of positive numbers: {positive_sum}")

# =============================================================================
# EXERCISE 6: WHILE LOOP - Collect Until Condition
# =============================================================================
print("\n📝 EXERCISE 6: Double a number until it exceeds 100")
print("-" * 60)

# Your solution here:
number = 5
iteration = 0
print(f"Starting number: {number}")
while number <= 100:
    number *= 2
    iteration += 1
    print(f"  After iteration {iteration}: {number}")
print(f"Final number: {number}")

# =============================================================================
# EXERCISE 7: NESTED FOR LOOPS - Multiplication Table
# =============================================================================
print("\n📝 EXERCISE 7: Generate a 5x5 multiplication table")
print("-" * 60)

# Your solution here:
for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        row += f"{i*j:3d} "
    print(row)

# =============================================================================
# EXERCISE 8: WHILE LOOP WITH MULTIPLE CONDITIONS
# =============================================================================
print("\n📝 EXERCISE 8: Countdown with limits")
print("-" * 60)

# Your solution here:
countdown = 20
steps = 0
max_steps = 5
print(f"Countdown from {countdown}:")
while countdown > 0 and steps < max_steps:
    print(f"  {countdown}")
    countdown -= 4
    steps += 1
print("Done!")

# =============================================================================
# EXERCISE 9: FOR LOOP - Find Maximum Value
# =============================================================================
print("\n📝 EXERCISE 9: Find maximum value in list")
print("-" * 60)

temperatures = [22, 25, 19, 28, 24, 30, 21]
print(f"Temperatures: {temperatures}")

# Your solution here:
max_temp = temperatures[0]
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
print(f"Maximum temperature: {max_temp}°C")

# =============================================================================
# EXERCISE 10: COMBINED - Process Data Stream
# =============================================================================
print("\n📝 EXERCISE 10: Process sensor data stream")
print("-" * 60)

sensor_stream = [45, 50, -999, 55, 60, -999, 65, 70]
threshold = 55
print(f"Sensor data: {sensor_stream}")
print(f"Threshold: {threshold}")

# Your solution here:
above_threshold = []
for reading in sensor_stream:
    if reading == -999:  # Skip error codes
        continue
    if reading > threshold:
        above_threshold.append(reading)

print(f"Readings above threshold: {above_threshold}")

# =============================================================================
# CHALLENGE EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("🏆 CHALLENGE EXERCISES")
print("=" * 60)

# Challenge 1: Fibonacci sequence using while loop
print("\n🎯 CHALLENGE 1: Generate Fibonacci sequence up to 100")
print("-" * 60)
a, b = 0, 1
fibonacci = [a, b]
while True:
    c = a + b
    if c > 100:
        break
    fibonacci.append(c)
    a, b = b, c
print(f"Fibonacci sequence: {fibonacci}")

# Challenge 2: Prime number checker
print("\n🎯 CHALLENGE 2: Find all prime numbers between 1 and 30")
print("-" * 60)
primes = []
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f"Prime numbers: {primes}")

# Challenge 3: Pattern printing
print("\n🎯 CHALLENGE 3: Print a number triangle")
print("-" * 60)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "=" * 60)
print("✅ ALL EXERCISES COMPLETED!")
print("=" * 60)
