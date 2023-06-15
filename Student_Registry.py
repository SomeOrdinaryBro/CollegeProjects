students = [
    {
        "Student_id": 1011,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS3U",
        "mark": 95
    },
    {
        "Student_id": 1021,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MCR3U",
        "mark": 88
    },
    {
        "Student_id": 1021,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS3U",
        "mark": 33
    },
    {
        "Student_id": 1031,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SPH3U",
        "mark": 100
    },
    {
        "Student_id": 1031,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 80
    },
    {
        "Student_id": 1041,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 99
    },
    {
        "Student_id": 1051,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MHF4U",
        "mark": 86
    },
    {
        "Student_id": 1061,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MPM2D",
        "mark": 75
    },
    {
        "Student_id": 1071,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS2O",
        "mark": 78
    },
    {
        "Student_id": 1081,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SCH3U",
        "mark": 81
    },
    {
        "Student_id": 1091,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 100
    },
    {
        "Student_id": 1012,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 79
    },
    {
        "Student_id": 1013,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MHF4U",
        "mark": 99
    },
    {
        "Student_id": 1014,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SPH4U",
        "mark": 98
    },
    {
        "Student_id": 1015,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MCV4U",
        "mark": 89
    },
    {
        "Student_id": 1016,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SPH3U",
        "mark": 80
    },
    {
        "Student_id": 1017,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SCH3U",
        "mark": 65
    },
    {
        "Student_id": 1018,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SPH4U",
        "mark": 88
    },
    {
        "Student_id": 1019,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 69
    },
    {
        "Student_id": 1022,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 43
    },
    {
        "Student_id": 1023,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MHF4U",
        "mark": 90
    },
    {
        "Student_id": 1024,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MCV4U",
        "mark": 49
    },
    {
        "Student_id": 1025,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SPH4U",
        "mark": 99
    },
    {
        "Student_id": 1026,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SCH4U",
        "mark": 87
    },
    {
        "Student_id": 1027,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS3U",
        "mark": 99
    },
    {
        "Student_id": 1028,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS4U",
        "mark": 100
    },
    {
        "Student_id": 1029,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MCV4U",
        "mark": 77
    },
    {
        "Student_id": 1032,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MCV4U",
        "mark": 29
    },
    {
        "Student_id": 1033,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MCR3U",
        "mark": 69
    },
    {
        "Student_id": 1034,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SCH3U",
        "mark": 47
    },
    {
        "Student_id": 1035,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "SPH3U",
        "mark": 94
    },
    {
        "Student_id": 1036,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "ICS3U",
        "mark": 8
    },
    {
        "Student_id": 1037,
        "student_first_name": "",
        "student_last_name": "",
        "course_code": "MDM4U",
        "mark": 60
    }
]

def add_student():
    """Add a new student to the registry."""
    student = {}
    student['student_first_name'] = input("Enter student first name: ")
    student['student_last_name'] = input("Enter student last name: ")
    student['Student_id'] = int(input("Enter student ID: "))  # Fixed capitalization of 'Student_id'
    student['course_code'] = input("Enter student course code: ")
    student['mark'] = int(input("Enter student mark: "))
    students.append(student)
    print("Student added successfully.")

def edit_student():
    """Edit student details."""
    student_id = int(input("Enter student ID to edit: "))
    found = False
    for student in students:
        if student['student_id'] == student_id:
            student['student_first_name'] = input("Enter new student first name: ")
            student['student_last_name'] = input("Enter new student last name: ")
            student['course_code'] = input("Enter new student course code: ")
            student['mark'] = int(input("Enter new student mark: "))
            print("Student details updated successfully.")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student():
    """Delete a student from the registry."""
    student_id = int(input("Enter student ID to delete: "))
    found = False
    for student in students:
        if student['Student_id'] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            found = True
            break
    if not found:
        print("Student not found.")


def report_all():
    """Generate a report of all students."""
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("Name:", student['student_first_name'], student['student_last_name'])
            print("ID:", student['Student_id'])
            print("Course:", student['course_code'])
            print("Mark:", student['mark'])
            print("---------------------")

def report_by_course():
    """Generate a report of students by course."""
    course = input("Enter course name: ")
    found = False
    for student in students:
        if student['course_code'] == course:
            print("Name:", student['student_first_name'], student['student_last_name'])
            print("ID:", student['Student_id'])
            print("---------------------")
            found = True
    if not found:
        print("No students found for the given course.")


def report_by_student():
    """Generate a report for a specific student."""
    student_id = input("Enter student ID: ")
    found = False
    for student in students:
        if student['id'] == student_id:
            print("Name:", student['name'])
            print("ID:", student['id'])
            print("Course:", student['course'])
            print("---------------------")
            found = True
            break
    if not found:
        print("Student not found.")

def special_report_failed_courses():
    """Generate a report of students who failed one or more courses."""
    failed_students = []
    for student in students:
        mark = student['mark']  # Fixed key from 'marks' to 'mark'
        if mark < 50:
            failed_students.append(student)
    if len(failed_students) == 0:
        print("No students failed any courses.")
    else:
        for student in failed_students:
            print("Name:", student['student_first_name'], student['student_last_name'])
            print("ID:", student['Student_id'])
            print("---------------------")


def special_report_highest_average():
    """Generate a report for the student with the highest average."""
    if len(students) == 0:
        print("No students found.")
    else:
        highest_average = 0
        highest_student = None
        for student in students:
            marks = student['marks']
            total_marks = sum(marks.values())
            average = total_marks / len(marks)
            if average > highest_average:
                highest_average = average
                highest_student = student
        if highest_student is not None:
            print("Student with the highest average:")
            print("Name:", highest_student['name'])
            print("ID:", highest_student['id'])
            print("Average:", highest_average)
        else:
            print("No students found.")

def special_report_lowest_average():
    """Generate a report for the student with the lowest average."""
    if len(students) == 0:
        print("No students found.")
    else:
        lowest_average = float('inf')
        lowest_student = None
        for student in students:
            marks = student['marks']
            total_marks = sum(marks.values())
            average = total_marks / len(marks)
            if average < lowest_average:
                lowest_average = average
                lowest_student = student
        if lowest_student is not None:
            print("Student with the lowest average:")
            print("Name:", lowest_student['name'])
            print("ID:", lowest_student['id'])
            print("Average:", lowest_average)
        else:
            print("No students found.")

def special_report_top_mark_by_course():
    """Generate a report for the top student in each course."""
    if len(students) == 0:
        print("No students found.")
    else:
        courses = set([student['course'] for student in students])
        for course in courses:
            top_student = None
            top_mark = 0
            for student in students:
                if student['course'] == course:
                    marks = student['marks']
                    max_mark = max(marks.values())
                    if max_mark > top_mark:
                        top_mark = max_mark
                        top_student = student
            if top_student is not None:
                print("Top student in", course, ":")
                print("Name:", top_student['name'])
                print("ID:", top_student['id'])
                print("Mark:", top_mark)
            else:
                print("No students found for", course)

def main():
    while True:
        print("------Braemar College student registry system ------")
        print("A. Add student")
        print("B. Edit student")
        print("C. Delete student")
        print("D. Report")
        print(" 1) All")
        print(" 2) By Course")
        print(" 3) By Student")
        print("E. Special Report")
        print(" 1) Students who failed one or more courses")
        print(" 2) Student whose Average is the highest in school")
        print(" 3) Student whose Average is lowest in School")
        print(" 4) Students who got top mark in each course")
        print("Q. Quit")

        choice = input("Enter one of these options (A-E or Q): ")

        if choice == 'A':
            add_student()
        elif choice == 'B':
            edit_student()
        elif choice == 'C':
            delete_student()
        elif choice == 'D':
            report_choice = input("Enter report option (1-3): ")
            if report_choice == '1':
                report_all()
            elif report_choice == '2':
                report_by_course()
            elif report_choice == '3':
                report_by_student()
            else:
                print("Invalid report option.")
        elif choice == 'E':
            special_report_choice = input("Enter special report option (1-4): ")
            if special_report_choice == '1':
                special_report_failed_courses()
            elif special_report_choice == '2':
                special_report_highest_average()
            elif special_report_choice == '3':
                special_report_lowest_average()
            elif special_report_choice == '4':
                special_report_top_mark_by_course()
            else:
                print("Invalid special report option.")
        elif choice == 'Q':
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")

    print("Program exited.")

if __name__ == '__main__':
    main()
