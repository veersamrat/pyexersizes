exp_list = [2200,2350,2600,2130,2190]

print(f'In Feb, {exp_list[1]-exp_list[0]} dollars you spent extra compare to January')
print(f"{exp_list[0]+exp_list[1]+exp_list[2]} dollers expense in first quarter (first three months) of the year")
print(f"Did you spent exactly 2000 dollars in any month:{2000 in exp_list}")
exp_list.append(1980)
print(f"{exp_list}")
exp_list[3] = exp_list[3]-200
print(f"{exp_list}")
