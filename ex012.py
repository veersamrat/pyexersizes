ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

# new_dict = {value: key for key, value in ascii_dict.items()}
new_dict ={}
for key,val in ascii_dict.items():
    new_dict.update({val:key})
print(new_dict)




