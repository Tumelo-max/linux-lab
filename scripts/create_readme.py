# Read Lab_Summary.txt and create README.md

input_file = "../Lab_Summary.txt"
output_file = "../README.md"

with open(input_file, "r") as f:
    content = f.read()

# Optional: add a title at the top for GitHub README
with open(output_file, "w") as f:
    f.write("# Linux & Networking Labs Portfolio\n\n")
    f.write(content)

print(f"README.md created at {output_file}")
