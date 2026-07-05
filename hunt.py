import re
from collections import defaultdict

# 1. Open and read the network traffic log
with open("network_traffic.log") as log_file:
    lines = log_file.readlines()

# 2. Parse each line into timestamp, source IP, and destination IP:port
line_pattern = re.compile(
    r"(\d{2}:\d{2}:\d{2})\s+(\d+\.\d+\.\d+\.\d+)\s+->\s+(\S+)\s+\d+\s+bytes"
)
pair_counts = defaultdict(int)
pair_timestamps = defaultdict(list)

for line in lines:
    match = line_pattern.match(line.strip())
    if not match:
        continue
    timestamp, source_ip, destination = match.groups()
    pair = (source_ip, destination)
    pair_counts[pair] += 1
    pair_timestamps[pair].append(timestamp)

# 3. Find the (source -> destination:port) pair with the most connections
suspect_pair = max(pair_counts, key=pair_counts.get)
connection_count = pair_counts[suspect_pair]
timestamps = pair_timestamps[suspect_pair]

# 4. Compute average seconds between consecutive connections
def to_seconds(ts):
    hours, minutes, seconds = map(int, ts.split(":"))
    return hours * 3600 + minutes * 60 + seconds

stamp_seconds = [to_seconds(ts) for ts in timestamps]
gaps = [stamp_seconds[i + 1] - stamp_seconds[i] for i in range(len(stamp_seconds) - 1)]
avg_seconds = sum(gaps) / len(gaps) if gaps else 0.0

# 5. Print the beaconing suspect and its connection timeline
print("=== Beaconing Suspect ===")
print(f"{suspect_pair[0]} -> {suspect_pair[1]}")
print(f"Connections: {connection_count}")
print(f"Average seconds between connections: {avg_seconds:.1f}")
print("Timestamps:")
for ts in timestamps:
    print(f"  {ts}")
