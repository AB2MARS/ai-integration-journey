# --- DAY 3: Integration Router Logic ---

# 1. Capture system metrics
print("--- [SYS_MONITOR] Starting Check ---")
system_load = int(input("Enter CPU Load % (0-100): "))
status_code = int(input("Enter HTTP Status Code (e.g., 200, 404, 500): "))

# 2. The Decision Gate (The heart of your future AI Agent)
if system_load > 90:
    action = "CRITICAL: Triggering auto-scale/failover."
    label = "🔴"
elif 70 <= system_load <= 90 and status_code == 200:
    action = "WARNING: System heavy but operational."
    label = "🟡"
elif status_code >= 500:
    action = "ALERT: Gateway Error detected. Checking MCP logs..."
    label = "🟠"
else:
    action = "OPTIMAL: No action required."
    label = "🟢"

# 3. Output the result
print(f"\n[RESULT] {label} {action}")

# 4. Infrastructure "Sanity Check" (Pydantic-style logic)
is_valid_packet = (0 <= system_load <= 100)
print(f"Packet Integrity Verified: {is_valid_packet}")

# --- Modern Python 3.13 "Match-Case" Router ---

status = int(input("Enter System Status Code: "))

match status:
    case 200 | 201:
        print("✅ Traffic Authorized: Proceeding to AI Agent.")
    case 401 | 403:
        print("🔒 Security Block: Unauthorized Access. Logged.")
    case 404:
        print("🔎 Resource Missing: Checking backup storage...")
    case 500 | 502 | 503:
        print("💣 Infrastructure Error: Triggering failover protocol.")
    case _:
        print("❓ Unknown Status: Escalating to Human.")