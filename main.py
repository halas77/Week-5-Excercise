students = [ 

    {'name': 'Alemayehu', 'score': 85}, 

    {'name': 'Nathan', 'score': 92}, 

    {'name': 'Azeb', 'score': 78}, 

    {'name': 'Hailu', 'score': 95}, 

    {'name': 'Gete', 'score': 88}, 

    {'name': 'Abigiya', 'score': 75}, 

    {'name': 'Tesfa', 'score': 90}, 

    {'name': 'Desta', 'score': 82}, 

    {'name': 'Tsinat', 'score': 89}, 

    {'name': 'Zerihun', 'score': 93} 

] 

# Initialize variables to keep track of the highest score and corresponding student
highest_score = 0
highest_scorer = None

# Iterate through the list of students
for stud in students:
    if stud['score'] > highest_score:
        highest_score = stud['score']
        highest_scorer = stud

# Print the name of the highest scorer
print(f"The student who scored the highest is: {highest_scorer['name']}")
