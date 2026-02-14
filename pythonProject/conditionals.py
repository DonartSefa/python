age = 18

if age>=18:
    print("you can vote")
else:
    print("You can't vote")

temperatura=28

if temperatura>30:
    print("It's a hot day stay hydrated.")
elif temperatura>=20 or temperatura <=30:
    print("The weather is pleasent.")
else :
    print("It's a cold day")

student_gpa = 4.5
student_score = 75

if student_gpa >=3.5:
    if student_score>=50 and student_score<=65:
        print("Student with these scores are eligible for a partial schoolship")
    elif student_score>65:
        print("Student with these scores are eligible for a schoolarship")
    else:
        print("Student with these scores are not eligible for a schoolarship")
else:
    print("Student gpa and test scores are not eligible for a scholarship")