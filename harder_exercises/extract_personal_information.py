number_of_people = int(input())

for i in range(number_of_people):
    man_info = input()
    name = ""
    age = ""

    name_start = man_info.find("@")
    name_end = man_info.find("|")

    if name_start != -1 and name_end != -1:
        name = man_info[name_start + 1:name_end]

    age_start = man_info.find("#")
    age_end = man_info.find("*")

    if age_start != -1 and age_end != -1:
        age = man_info[age_start + 1:age_end]

    if name and age:
        print(f"{name} is {age} years old.")
