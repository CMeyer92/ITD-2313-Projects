initial_population = float(input("Insert initial population census: "))
growth_rate = float(input("Insert growth rate value: "))
hours_per_growth = float(input("Insert hours per growth: "))
total_hours = float(input("Insert total hours of growth: "))

num_periods = total_hours / hours_per_growth

final_population = initial_population * (growth_rate ** num_periods)

print(int(final_population))
