# --- DAY 2: Variables and Data Types ---

# 1. String (Text) - Used for names, paths, or status
system_name = input("Enter the system name: ")

# 2. Integer (Whole Numbers) - Used for counts or ports
port_number = int(input("Enter the port number: "))

# 3. Float (Decimals) - Used for timestamps or precise values
uptime_hours = float(input("Enter uptime hours: "))

# 4. Boolean (True/False) - Used for logic gates
is_active = True

# Displaying the "Payload" using an F-String (The pro way to format text)
print(f"--- {system_name} Report ---")
print(f"Status Active: {is_active}")
print(f"Listening on Port: {port_number}")
print(f"Current Uptime: {uptime_hours} hours")
print(f"if we double the ports, we would need: {port_number *2}")

# Simple Logic Check
if is_active:
    print("✅ SYSTEM READY")