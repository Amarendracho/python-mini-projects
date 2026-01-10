
def student_grade_report():
    student_name = input("Please enter your name: ").strip().lower()

    number_of_sub = int(input("Please enter number of subjects: "))
    if number_of_sub <= 0:
        print("Number of subjects must be greater than 0")
        return

    total_marks = 0
    for i in range(number_of_sub):
        marks_individual = int(input(f"Enter marks for subject {i+1}: "))
        total_marks += marks_individual

    average = total_marks / number_of_sub

    if average >= 90:
        grade = "Toper"
    elif average >= 75:
        grade = "Distinction"
    elif average >= 60:
        grade = "First class"
    elif average >= 50:
        grade = "Second class"
    elif average >= 40:
        grade = "Third class"
    else:
        grade = "Fail"

    print("\n--- Student Report ---")
    print(f"Name           : {student_name}")
    print(f"Total Marks    : {total_marks}")
    print(f"Average Marks  : {average:.2f}")
    print(f"Grade          : {grade}")


student_grade_report()