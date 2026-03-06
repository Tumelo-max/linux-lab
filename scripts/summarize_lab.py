import os

# 1️⃣ List of lab folders
lab_folders = [
    "../lab1",
    "../lab2",
    "../lab3",
    "../lab4",
    "../lab5",
    "../lab6_system_monitoring",
    "../lab7_port_scanning",
    "../lab7_nmap",
    "../lab8_tcpdump",
    "../lab8_log_analyzer",
    "../teraco_lab"  # optional, add if you want
]

# 2️⃣ Path to README.md
readme_path = "../README.md"

# 3️⃣ Start writing README
with open(readme_path, "w") as readme:
    readme.write("# Linux & Cybersecurity Lab Portfolio\n\n")
    readme.write("This README contains outputs from my Linux & Networking labs.\n\n")
    readme.write("="*60 + "\n\n")
    
    for lab in lab_folders:
        if os.path.exists(lab):
            readme.write(f"## Contents of {os.path.basename(lab)}\n\n")
            for file_name in os.listdir(lab):
                if file_name.endswith(".txt"):
                    file_path = os.path.join(lab, file_name)
                    readme.write(f"### {file_name}\n\n")
                    with open(file_path, "r") as f:
                        readme.write(f"```\n{f.read()}\n```\n\n")
            readme.write("-"*60 + "\n\n")
        else:
            readme.write(f"## {os.path.basename(lab)} does not exist yet.\n\n")

print(f"✅ README.md updated successfully at {readme_path}")import os

# Path to README
summary_file = "../README.md"

with open(summary_file, "w") as summary:
    summary.write("# Linux & Cybersecurity Labs Portfolio\n")
    summary.write("All outputs from my hands-on labs, updated automatically.\n\n")
    summary.write("="*50 + "\n\n")

    for lab in lab_folders:
        summary.write(f"## {os.path.basename(lab).replace('_', ' ').title()}\n")
        for file_name in os.listdir(lab):
            if file_name.endswith(".txt") or file_name.endswith(".py"):
                file_path = os.path.join(lab, file_name)
                summary.write(f"\n### {file_name}\n")
                with open(file_path, "r") as f:
                    summary.write("```\n")
                    summary.write(f.read())
                    summary.write("\n```\n")
        summary.write("\n" + "-"*50 + "\n\n")

print(f"README.md updated with all lab outputs at {summary_file}")ab_folders = ["../lab1", "../lab2", "../lab3", "../lab4", "../lab5", "../lab6_system_monitoring", "../lab7_port_scanning", "../lab8_log_analyzer"]lab_folders = ["../lab1", "../lab2", "../lab3", "../lab4", "../lab5", "../lab6_system_monitoring", "../lab7_port_scanning", "../lab8_log_analyzer"]import os

# List all lab folders
lab_folders = ["../lab1", "../lab2", "../lab3", "../lab4"]

# Output file for summary
summary_file = "../README.md"

with open(summary_file, "w") as summary:
    summary.write("# Linux & Networking Labs Portfolio\n")
    summary.write("This README contains outputs from Labs 1 to 4.\n\n")
    
    for lab in lab_folders:
        summary.write(f"## {os.path.basename(lab).capitalize()}\n")
        summary.write("-" * 40 + "\n")
        for file_name in os.listdir(lab):
            if file_name.endswith(".txt"):
                file_path = os.path.join(lab, file_name)
                summary.write(f"\n### {file_name}\n")
                with open(file_path, "r") as f:
                    summary.write(f"```\n{f.read()}\n```\n")
        summary.write("\n\n")

print(f"README updated with Lab 1 to Lab 4 outputs at {summary_file}")import os

# List all lab folders
lab_folders = ["../lab1", "../lab2", "../lab3", "../lab4"]

# Output file for summary
summary_file = "../README.md"

with open(summary_file, "w") as summary:
    summary.write("# Linux & Networking Labs Portfolio\n")
    summary.write("This README contains outputs from Labs 1 to 4.\n\n")
    
    for lab in lab_folders:
        summary.write(f"## {os.path.basename(lab).capitalize()}\n")
        summary.write("-" * 40 + "\n")
        for file_name in os.listdir(lab):
            if file_name.endswith(".txt"):
                file_path = os.path.join(lab, file_name)
                summary.write(f"\n### {file_name}\n")
                with open(file_path, "r") as f:
                    summary.write(f"```\n{f.read()}\n```\n")
        summary.write("\n\n")

print(f"README updated with Lab 1 to Lab 4 outputs at {summary_file}")ximport os

# Path to your lab folders
lab_folders = ["../lab1", "../lab2"]

summary_file = "../Lab_Summary.txt"

with open(summary_file, "w") as summary:
    summary.write("Linux & Networking Lab Summary\n")
    summary.write("="*40 + "\n\n")

    for lab in lab_folders:
        summary.write(f"Contents of {lab}:\n")
        for file_name in os.listdir(lab):
            if file_name.endswith(".txt"):
                file_path = os.path.join(lab, file_name)
                summary.write(f"\n--- {file_name} ---\n")
                with open(file_path, "r") as f:
                    summary.write(f.read())
        summary.write("\n" + "-"*40 + "\n\n")

print(f"Summary created at {summary_file}")
