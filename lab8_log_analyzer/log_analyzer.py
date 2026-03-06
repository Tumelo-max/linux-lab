import os

log_file = "system_logs.txt"

with open(log_file, "w") as f:
    os.system("dmesg > system_logs.txt")

with open(log_file, "r") as f:
    lines = f.readlines()

print("Total log lines:", len(lines))

error_lines = [line for line in lines if "error" in line.lower()]

print("Error entries found:", len(error_lines))
