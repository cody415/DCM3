# File Reading Demonstration: Different Methods

# Step 1: Create a sample file with some content
with open("students.txt", "w") as f:
    f.write("Line 1: Welcome to File Handling\n")
    f.write("Line 2: Python makes it easy\n")
    f.write("Line 3: Practice is important\n")
    f.write("Line 4: Keep experimenting\n")

print("Sample file created.\n")

# Step 2: Read entire file using read()
with open("students.txt", "r") as f:
    content = f.read()
    print("Method 1: Using read()\n", content)

# Step 3: Read file line by line using readline()
with open("students.txt", "r") as f:
    print("\nMethod 2: Using readline()")
    line1 = f.readline()
    line2 = f.readline()
    print(line1.strip())
    print(line2.strip())

# Step 4: Read all lines into a list using readlines()
with open("students.txt", "r") as f:
    lines = f.readlines()
    print("\nMethod 3: Using readlines()")
    print(lines)

# Step 5: Iterate directly over the file object
with open("students.txt", "r") as f:
    print("\nMethod 4: Iterating over file object")
    for line in f:
        print(line.strip())

# Step 6: Read fixed number of characters
with open("students.txt", "r") as f:
    print("\nMethod 5: Reading fixed number of characters")
    first_10 = f.read(10)
    print("First 10 characters:", first_10)
