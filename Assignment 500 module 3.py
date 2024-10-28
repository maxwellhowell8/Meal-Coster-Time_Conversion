# Part 1: Meal Total Calculation
# Get the food charge from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip and tax amounts
tip = food_charge * 0.18
tax = food_charge * 0.07

# Calculate the total price
total_price = food_charge + tip + tax

# Display the results
print("\n--- Meal Total ---")
print(f"Tip: ${tip:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Price: ${total_price:.2f}")

# Part 2: 24-Hour Alarm Calculation
# Get the current time in hours and hours to wait
current_time = int(input("\nEnter the current time (0-23): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + wait_hours) % 24

# Display the time the alarm will go off
print("\n--- Alarm Time ---")
print(f"The alarm will go off at: {alarm_time}:00")

