# Exercise 1
students = ['Victor', 'Sam', 'Lew', 'Liz', 'Larry']

# print(students[1])
# print(students[-1])

# Exercise 2
foods = ('coconut aminos', 'green onions', 'chili paste', 'noodles', 'garlic')

# for food in foods:
#   message = f'{food} is a good food'

#   print(message)

# type_of_range = type(range(5))

# print(type_of_range)

# Exercise 3
# for index in range(-2, 0):
#   print(foods[index])

# Exercise 4
home_town = {
  'city': 'San Diego',
  'state': 'California',
  'population': 1500000
}

# description = f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}'

# print(description)

# Exercise 5
# for key in home_town:
#   output = f'{key} = {home_town[key]}'
  
#   print(output)

# Exercise 6
# students = ('Tina', 'Tim', 'Terry', 'Tyrone', 'Tammy')
# foods = ('chili paste', 'coconut aminos', 'garlic', 'green onions', 'peanuts')
# cohort = []

# for index, student in enumerate(students):
#   student_obj = {
#     'student': student,
#     'fav_food': foods[index]
#   }

#   cohort.append(student_obj)

# for student in students:
#   student_obj = {
#     'student': student,
#     'fav_food': 'pizza'
#   }

#   cohort.append(student_obj)

# print(cohort)

# Exercise 7
# students = ('Tina', 'Tim', 'Terry', 'Tyrone', 'Tammy')
# awesome_students = [f'{student} is awesome!' for student in students]

# for message in awesome_students:
#   print(message)

# Exercise 8
# foods = ('ground meat', 'tomato', 'cilantro', 'cayanne pepper', 'mint', 'onion', 'garlic', 'broth')


# for food in foods:
#   letter_as = [letter for letter in food if letter == 'a']

#   # If the length of the array is zero, conditional will be False
#   if len(letter_as): print(food)

