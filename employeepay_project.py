wage = float(input("Input Employee Hourly Wage: "))
regular_hours = float(input("Input Employee Hours Worked: "))
overtime_hours = float(input("Input Overtime Hours: "))

base_pay = wage * regular_hours
overtime_pay = overtime_hours * (1.5 * wage)

total_pay = base_pay + overtime_pay

print(round(total_pay, 2))
