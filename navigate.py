filename = input("Enter the filename: ")

with open(filename, "r") as file:
    lines =  file.readlines()

while True:
    print("The file has", len(lines), "lines.")
    line_number = int(input("Enter a line number (0 to quit): "))

    if line_number == 0:
        print("Exiting program.")
        break
    elif 1 <= line_number <= len(lines):
        print(lines[line_number - 1].rstrip())
    else:
        print("Invalid line number.")
