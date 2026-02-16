starting_salary = float(input("Input starting salary: "))
percent_increase = float(input("Input percentage increase: "))
years = int(input("Input years employed: "))

salary = starting_salary

print("Year\tSalary")

for year in range(1, years + 1):
    print(year, "\t", format(salary, ".2f"))
    salary = salary * (1 + percent_increase / 100)
