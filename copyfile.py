source_name = input("Enter the source file name: ")
dest_name = input("Enter the destination name file: ")

with open(source_name, "r") as source_file:
    contents = source_file.read()

with open(dest_name, "w") as dest_file:
    dest_file.write(contents)

print("File copied successfully.")
