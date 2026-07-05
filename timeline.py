from datetime import datetime

KEY_MARKERS = ("SUCCESS LOGIN", ".locked", "READ_ME")

# 1. Read all lines from both log files
with open("auth_events.log") as auth_file:
    auth_lines = auth_file.readlines()
with open("file_events.log") as file_file:
    file_lines = file_file.readlines()

# 2. Merge events into one list of (timestamp, line) tuples
events = []
for line in auth_lines + file_lines:
    line = line.rstrip("\n")
    if not line.strip():
        continue
    timestamp = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
    events.append((timestamp, line))

# 3. Sort events in chronological order
events.sort(key=lambda item: item[0])

# 4. Print the merged timeline, flagging key events
print("=== Unified Timeline ===")
for _, line in events:
    if any(marker in line for marker in KEY_MARKERS):
        print(f"{line} *** KEY EVENT ***")
    else:
        print(line)

# 5. Dwell time: minutes from first successful malicious login to first .locked file
first_success = next(
    ts for ts, line in events if "SUCCESS LOGIN" in line and "185.220.101.47" in line
)
first_locked = next(ts for ts, line in events if ".locked" in line)
dwell_minutes = (first_locked - first_success).total_seconds() / 60
print(
    f"\nDwell time (first successful malicious login -> first .locked file): "
    f"{dwell_minutes:.1f} minutes"
)
