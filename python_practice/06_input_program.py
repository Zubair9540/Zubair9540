# person_a_name = input("Enter your name: ")
# person_a_age = input("Enter your age: ")

# person_b_name = input("Enter your name: ")
# person_b_age = input("Enter your age: ")

# if person_a_age > person_b_age:
#     print(person_a_name, "is older than", person_b_name)
# else:
#     print(person_b_name, "younger than", person_b_name)


name_a = str(input("Enter your name: "))
height_a = float(input("Enter your height in meter: "))
weight_a = float(input("Enter you wight in kg: "))
bmi_a = weight_a / (height_a)**2
print(name_a, "your bmi is: ", bmi_a)
