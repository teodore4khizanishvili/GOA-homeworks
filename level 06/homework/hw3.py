user_name = input("Please enter your first name: ")
age = int(input("Please enter your age: "))
is_student = input("Please enter if you are a student or not (True/False): ") == "True"

print(is_student and age >= 18)