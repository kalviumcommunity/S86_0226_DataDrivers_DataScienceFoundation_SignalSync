"""
Loops and Iteration Demonstration
===================================
This file demonstrates the use of for and while loops in Python
for iterative data processing.
"""

print("=" * 60)
print("LOOPS AND ITERATION DEMONSTRATION")
print("=" * 60)

# =============================================================================
# 1. USING FOR LOOPS FOR ITERATION
# =============================================================================
print("\n" + "=" * 60)
print("1. FOR LOOPS - Iterating Over Sequences")
print("=" * 60)

# Example 1.1: Iterating over a range of numbers
print("\n--- Example 1.1: Iterating over a range ---")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  Count: {i}")

# Example 1.2: Iterating over a list
print("\n--- Example 1.2: Iterating over a list ---")
traffic_signals = ["Red", "Yellow", "Green", "Yellow", "Red"]
print("Traffic signal sequence:")
for signal in traffic_signals:
    print(f"  Signal: {signal}")

# Example 1.3: Iterating with index and value
print("\n--- Example 1.3: Using enumerate for index and value ---")
sensors = ["Speed", "Temperature", "Pressure", "Humidity"]
print("Sensor list with indices:")
for index, sensor in enumerate(sensors):
    print(f"  Sensor {index}: {sensor}")

# Example 1.4: Processing data with for loop
print("\n--- Example 1.4: Processing numerical data ---")
vehicle_speeds = [45, 60, 72, 55, 80, 65]
print(f"Vehicle speeds: {vehicle_speeds}")
total_speed = 0
for speed in vehicle_speeds:
    total_speed += speed
average_speed = total_speed / len(vehicle_speeds)
print(f"Average speed: {average_speed:.2f} km/h")

# Example 1.5: For loop with range and step
print("\n--- Example 1.5: Using range with step ---")
print("Even numbers from 0 to 10:")
for num in range(0, 11, 2):
    print(f"  {num}")

# =============================================================================
# 2. USING WHILE LOOPS FOR CONDITION-BASED REPETITION
# =============================================================================
print("\n" + "=" * 60)
print("2. WHILE LOOPS - Condition-Based Repetition")
print("=" * 60)

# Example 2.1: Basic while loop
print("\n--- Example 2.1: Simple countdown ---")
counter = 5
print("Countdown starting:")
while counter > 0:
    print(f"  {counter}...")
    counter -= 1
print("  Liftoff!")

# Example 2.2: While loop with condition checking
print("\n--- Example 2.2: Processing until condition is met ---")
data_collected = 0
target_samples = 10
print(f"Collecting {target_samples} data samples:")
while data_collected < target_samples:
    data_collected += 1
    print(f"  Sample {data_collected} collected")
print(f"Data collection complete! Total samples: {data_collected}")

# Example 2.3: While loop with user input simulation
print("\n--- Example 2.3: Monitoring sensor threshold ---")
sensor_value = 20
threshold = 50
increment = 8
print(f"Starting sensor value: {sensor_value}")
print(f"Threshold: {threshold}")
while sensor_value < threshold:
    sensor_value += increment
    print(f"  Sensor reading: {sensor_value}")
print(f"Threshold reached! Final value: {sensor_value}")

# Example 2.4: While loop for accumulation
print("\n--- Example 2.4: Accumulating values ---")
accumulated_sum = 0
current_value = 1
print("Summing numbers until sum exceeds 50:")
while accumulated_sum <= 50:
    accumulated_sum += current_value
    print(f"  Added {current_value}, sum is now: {accumulated_sum}")
    current_value += 1
print(f"Final sum: {accumulated_sum}")

# =============================================================================
# 3. CONTROLLING LOOP FLOW (BREAK AND CONTINUE)
# =============================================================================
print("\n" + "=" * 60)
print("3. CONTROLLING LOOP FLOW")
print("=" * 60)

# Example 3.1: Using break to exit early
print("\n--- Example 3.1: Using break to exit loop ---")
print("Searching for a specific sensor in list:")
sensors_list = ["Temperature", "Pressure", "Humidity", "Speed", "Altitude"]
target_sensor = "Humidity"
for sensor in sensors_list:
    print(f"  Checking: {sensor}")
    if sensor == target_sensor:
        print(f"  Found {target_sensor}! Stopping search.")
        break
else:
    print(f"  {target_sensor} not found in list.")

# Example 3.2: Using continue to skip iterations
print("\n--- Example 3.2: Using continue to skip iterations ---")
print("Processing sensor readings (skipping invalid readings):")
sensor_readings = [25, -999, 30, 28, -999, 32, 27]
valid_readings = []
for reading in sensor_readings:
    if reading == -999:
        print(f"  Skipping invalid reading: {reading}")
        continue
    print(f"  Valid reading: {reading}")
    valid_readings.append(reading)
print(f"Valid readings collected: {valid_readings}")

# Example 3.3: Break in while loop
print("\n--- Example 3.3: Break in while loop ---")
print("Monitoring traffic until incident detected:")
traffic_flow = 100
iteration = 0
while True:
    iteration += 1
    traffic_flow -= 5
    print(f"  Iteration {iteration}: Traffic flow = {traffic_flow}")
    if traffic_flow < 70:
        print("  Incident detected! Traffic flow too low.")
        break
    if iteration >= 10:
        print("  Maximum iterations reached.")
        break

# Example 3.4: Continue in while loop
print("\n--- Example 3.4: Continue in while loop ---")
print("Processing data packets (skipping corrupted ones):")
packet_id = 0
max_packets = 8
corrupted_packets = [2, 5, 7]
while packet_id < max_packets:
    packet_id += 1
    if packet_id in corrupted_packets:
        print(f"  Packet {packet_id}: CORRUPTED - skipping")
        continue
    print(f"  Packet {packet_id}: Processed successfully")

# =============================================================================
# 4. AVOIDING INFINITE LOOPS
# =============================================================================
print("\n" + "=" * 60)
print("4. AVOIDING INFINITE LOOPS")
print("=" * 60)

# Example 4.1: Properly updating loop variable
print("\n--- Example 4.1: Correct loop termination ---")
print("GOOD PRACTICE: Loop variable is updated")
count = 0
max_iterations = 5
while count < max_iterations:
    print(f"  Iteration {count + 1}")
    count += 1  # IMPORTANT: Update the loop variable!
print("Loop completed successfully.")

# Example 4.2: Using a safety counter
print("\n--- Example 4.2: Using a safety counter ---")
print("Processing with safety limit:")
safety_counter = 0
max_safety_limit = 100
processing = True
simulated_condition = 0
while processing and safety_counter < max_safety_limit:
    safety_counter += 1
    simulated_condition += 10
    if simulated_condition >= 50:
        processing = False
        print(f"  Processing complete at iteration {safety_counter}")
if safety_counter >= max_safety_limit:
    print("  WARNING: Safety limit reached!")

# Example 4.3: Multiple exit conditions
print("\n--- Example 4.3: Multiple exit conditions ---")
print("Monitoring system with multiple stop conditions:")
temperature = 20
max_temp = 100
time_elapsed = 0
max_time = 15
while temperature < max_temp and time_elapsed < max_time:
    temperature += 8
    time_elapsed += 1
    print(f"  Time: {time_elapsed}s, Temp: {temperature}°C")
if temperature >= max_temp:
    print("Temperature limit reached!")
if time_elapsed >= max_time:
    print("Time limit reached!")

# Example 4.4: Demonstrating potential infinite loop (prevented)
print("\n--- Example 4.4: Preventing infinite loop ---")
print("EXPLANATION: Without proper update, this would loop forever")
print("WRONG: while x < 10: print(x)  # x never changes!")
print("RIGHT: while x < 10: print(x); x += 1  # x is updated")
x = 0
iteration_limit = 5  # Safety limit for demonstration
print(f"Safe demonstration (limited to {iteration_limit} iterations):")
while x < 10 and x < iteration_limit:
    print(f"  x = {x}")
    x += 1  # Proper update prevents infinite loop

# =============================================================================
# 5. PRACTICAL DATA PROCESSING EXAMPLES
# =============================================================================
print("\n" + "=" * 60)
print("5. PRACTICAL DATA PROCESSING SCENARIOS")
print("=" * 60)

# Example 5.1: Filtering data with for loop
print("\n--- Example 5.1: Filtering high-speed vehicles ---")
vehicle_speeds = [45, 80, 60, 95, 55, 70, 85, 50]
speed_limit = 70
speeding_vehicles = []
for speed in vehicle_speeds:
    if speed > speed_limit:
        speeding_vehicles.append(speed)
print(f"All speeds: {vehicle_speeds}")
print(f"Speed limit: {speed_limit} km/h")
print(f"Speeding vehicles: {speeding_vehicles}")

# Example 5.2: Data transformation with for loop
print("\n--- Example 5.2: Converting temperature readings ---")
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = []
print("Converting Celsius to Fahrenheit:")
for temp_c in celsius_temps:
    temp_f = (temp_c * 9/5) + 32
    fahrenheit_temps.append(temp_f)
    print(f"  {temp_c}°C = {temp_f}°F")

# Example 5.3: Data validation with while loop
print("\n--- Example 5.3: Validating data stream ---")
data_stream = [100, 105, 110, 95, 90, 85, 80, 75]
min_threshold = 85
valid_count = 0
index = 0
print(f"Checking data until value drops below {min_threshold}:")
while index < len(data_stream) and data_stream[index] >= min_threshold:
    print(f"  Index {index}: {data_stream[index]} - Valid")
    valid_count += 1
    index += 1
print(f"Valid consecutive readings: {valid_count}")

# Example 5.4: Nested loops for matrix processing
print("\n--- Example 5.4: Processing 2D data (nested loops) ---")
sensor_grid = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]
print("Sensor grid values:")
for row_index, row in enumerate(sensor_grid):
    for col_index, value in enumerate(row):
        print(f"  Position [{row_index}][{col_index}]: {value}")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Takeaways:
1. FOR LOOPS: Use when iterating over known sequences (lists, ranges)
2. WHILE LOOPS: Use when repetition depends on conditions
3. BREAK: Exit loop immediately
4. CONTINUE: Skip current iteration and continue with next
5. INFINITE LOOPS: Always ensure loop variables are updated properly
6. SAFETY: Use counters or multiple conditions to prevent infinite loops

Best Practices:
✓ Choose the right loop type for your task
✓ Always update loop variables in while loops
✓ Use meaningful variable names
✓ Keep loop logic simple and readable
✓ Test with small examples first
✓ Add safety limits for condition-based loops
""")

print("=" * 60)
print("DEMONSTRATION COMPLETE")
print("=" * 60)
