import re
from collections import Counter

# 1. Open and read the log file
with open("server_access.log") as log_file:
    lines = log_file.readlines()

# 2. Find every line containing 'FAILED LOGIN'
failed_login_lines = [line for line in lines if "FAILED LOGIN" in line]

# 3. Extract the IP address from each failed-login line
ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
ip_counts = Counter()

for line in failed_login_lines:
    match = ip_pattern.search(line)
    if match:
        ip_counts[match.group()] += 1

# 4. Counts are stored in ip_counts (Counter tallies each IP automatically)

# 5. Print a summary sorted from most to fewest failed attempts
print("=== Failed Login Summary ===")
for ip, count in sorted(ip_counts.items(), key=lambda item: (-item[1], item[0])):
    print(f"{ip}: {count} failed attempt(s)")
