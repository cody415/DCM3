# File Handling Demonstration: Access Modes

# Step 1: Create a sample file with initial content
with open("sample.txt", "w") as f:
    f.write("Hello Students!\nWelcome to File Handling.\n")

print("Step 1: File created with initial content.\n")

# Step 2: Read Mode (r)
with open("sample.txt", "r") as f:
    data = f.read()
    print("Step 2: Read Mode (r)\n", data)

# Step 3: Write Mode (w) - overwrites content
with open("sample.txt", "w") as f:
    f.write("This content overwrites the old one.\n")

print("\nStep 3: Write Mode (w) - content overwritten.\n")

# Step 4: Append Mode (a) - adds new content at the end
with open("sample.txt", "a") as f:
    f.write("This line is appended at the end.\n")

print("Step 4: Append Mode (a) - content appended.\n")

# Step 5: Read + Write Mode (r+)
with open("sample.txt", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write("Inserted at the beginning.\n" + content)

print("Step 5: Read + Write Mode (r+) - inserted at beginning.\n")

# Step 6: Write + Read Mode (w+)
with open("sample.txt", "w+") as f:
    f.write("Fresh start with w+ mode.\n")
    f.seek(0)
    print("Step 6: Write + Read Mode (w+)\n", f.read())

# Step 7: Append + Read Mode (a+)
with open("sample.txt", "a+") as f:
    f.write("Added using a+ mode.\n")
    f.seek(0)
    print("\nStep 7: Append + Read Mode (a+)\n", f.read())
