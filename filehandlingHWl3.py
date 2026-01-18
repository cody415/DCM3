# File Operations Demonstration

# Step 1: Create a sample file with initial content
with open("operations.txt", "w") as f:
    f.write("Line 1: Welcome to File Handling\n")
    f.write("Line 2: Python makes it easy\n")
    f.write("Line 3: Practice is important\n")

print("Step 1: File created with initial content.\n")

# Step 2: Read entire file
with open("operations.txt", "r") as f:
    print("Step 2: Read entire file using read()")
    print(f.read())

# Step 3: Read line by line
with open("operations.txt", "r") as f:
    print("\nStep 3: Read line by line using readline()")
    print(f.readline().strip())
    print(f.readline().strip())

# Step 4: Read all lines into a list
with open("operations.txt", "r") as f:
    print("\nStep 4: Read all lines using readlines()")
    lines = f.readlines()
    print(lines)

# Step 5: Append new content
with open("operations.txt", "a") as f:
    f.write("Line 4: This line is appended.\n")

print("\nStep 5: Append Mode - new line added.\n")

# Step 6: Overwrite content
with open("operations.txt", "w") as f:
    f.write("File overwritten with new content.\n")

print("Step 6: Write Mode - file overwritten.\n")

# Step 7: Read + Write Mode
with open("operations.txt", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write("Inserted at beginning.\n" + content)

print("Step 7: Read + Write Mode - content modified.\n")

# Step 8: Demonstrate file pointer
with open("operations.txt", "r") as f:
    print("Step 8: Using tell() and seek()")
    print("Initial pointer position:", f.tell())
    print("First 10 characters:", f.read(10))
    print("Pointer after reading 10 chars:", f.tell())
    f.seek(0)
    print("Pointer reset to:", f.tell())
    print("Reading again:", f.read(10))
