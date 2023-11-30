# Open the file
file_path = 'file.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    # Read the contents
    content = file.read()

    # Print the contents
    print(content)

# The file is automatically closed after the with block
