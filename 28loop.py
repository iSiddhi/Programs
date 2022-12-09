


aliens = []
strength = []

for i in range(5):
    first_name = input("Enter the alien name: ")
    last_name = input("Enter the alien strengh: ")
    aliens.append(first_name)
    strength.append(last_name)

overall_list = []
for i in range(len(aliens)):
    overall_list += [f"{aliens[i]} {strength[i]}"]
print(overall_list)