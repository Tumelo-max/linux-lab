import os
import subprocess

# Lab 2 folder
lab2_folder = "../lab2/outputs"

# Make sure folder exists
os.makedirs(lab2_folder, exist_ok=True)

# Commands to run and save
commands = {
    "ping_google": "ping -c 4 google.com",
    "traceroute_google": "traceroute google.com",
    "netstat": "netstat -tulnp",
    "ss": "ss -tulnp"
}

for name, cmd in commands.items():
    output_file = os.path.join(lab2_folder, f"{name}_results.txt")
    print(f"Running {cmd} → saving to {output_file}")
    with open(output_file, "w") as f:
        # Run command
        subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT)

print("Lab 2 automation completed!")
