import os

# Path to Lab 2 outputs
lab2_folder = "../lab2/outputs"

# README file (we'll append to it)
readme_file = "../README.md"

# Open README in append mode
with open(readme_file, "a") as readme:
    readme.write("\n## Lab 2 Outputs\n")
    readme.write("="*30 + "\n")

    # Go through all .txt files in lab2 outputs
    for file_name in os.listdir(lab2_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(lab2_folder, file_name)
            readme.write(f"\n--- {file_name} ---\n")
            with open(file_path, "r") as f:
                readme.write(f.read())  # append the content of each file

print(f"README.md updated with Lab 2 outputs!")
