# Number Grade to Letter Grade Converter
# Convert user input from string to numerical value
grade = float(input("What is your grade in the class? "))

# Define a function that stores numeric value into letter grade to be returned in print function
# Convert numerical grade to letter grade
def gradeconvert (grade):
  if grade <= 100 and grade >= 90:
    letter_grade = "A"
    return (letter_grade)
  elif grade < 90 and grade >= 80:
    letter_grade = "B"
    return (letter_grade)
  elif grade < 80 and grade >= 70:
    letter_grade = "C"
    return (letter_grade)
  elif grade < 70 and grade >= 60:
    letter_grade = "D"
    return (letter_grade)
  else:
    letter_grade = "F"
    return (letter_grade)

# Define a function that displays how far the user is from the next highest letter grade
# If grade is an A, display how far user is from a B
# If grade is a B, C, D, or F, display how far user is from the next highest letter grade
def nextgrade (grade):
  if grade <= 100 and grade >= 90:
    next = grade - 90.01
    return ("You are " + str(next) + " points away from a B")
  elif grade < 90 and grade >= 80:
    next = 90 - grade
    return ("You are " + str(next) + " points away from an A")
  elif grade < 80 and grade >= 70:
    next = 80 - grade
    return ("You are " + str(next) + " points away from an B")
  elif grade < 70 and grade >= 60:
    next = 70 - grade
    return ("You are " + str(next) + " points away from an C")
  elif grade < 60:
    next = 60 - grade
    return ("You are " + str(next) + " points away from an D")
  

# Define a function that gives the user an encouraging message depending on how well they are doing
# If grade is greater than 80 or at least a B, display a congratulations message
# If grade is less, display a message encouraging the user to work harder
def message (grade):
  if grade >= 80:
    return ("Keep up the great work!")
  else:
    return ("Keep your head up! Try to improve your skills!")

# Print statements and call return values from defined functions
print ("Your letter grade is: ", (gradeconvert (grade)))
print (nextgrade (grade))
print (message (grade))