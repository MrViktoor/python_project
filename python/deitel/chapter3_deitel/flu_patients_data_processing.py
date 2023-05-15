week = 7
total_num_of_infections = 0
average_num_of_infections_per_day = 0
min_num_of_infecton = []
max_num_of_infecton = []

for day in range(1,week+1):
    number_of_reported_infection = int(input("Enter number of reported infections for the day: "))
    total_num_of_infections += number_of_reported_infection
    average_num_of_infections_per_day = total_num_of_infections//week
    min_num_of_infecton.append(number_of_reported_infection)
    max_num_of_infecton.append(number_of_reported_infection)

print()
print("Total number of infections for the week is", total_num_of_infections)
print("Average number of infections in the week is", average_num_of_infections_per_day)
print("Minimum number of infection for the week is", min(min_num_of_infecton))
print("Maximum number of infection for the week is", max(max_num_of_infecton))
