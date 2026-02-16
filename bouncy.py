bounciness_index = 0.6

initial_height = float(input("Enter initial height: "))
num_bounces = int(input("Enter the number of bounces: "))

total_distance = 0
current_height = initial_height

for bounce in range(num_bounces):
    total_distance += current_height
    current_height *= bounciness_index
    total_distance += current_height

print(total_distance)

