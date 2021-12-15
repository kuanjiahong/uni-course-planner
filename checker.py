'''
This is a python program that is used to check for eligible 
HKU Comp Elective courses based on the courses taken by 
the student
'''

import csv

def check_semicolon(str):
    '''
    From the parameter str, the function checks
    if str has semicolon inside it
    return True if yes 
    else return Flase
    '''

    if ";" in str:
        return True
    else:
        return False



def clean_word(ls):
    '''
    This function is to clean the list ls being
    passed as the argument.

    First it will loop through the list and remove 
    any the semicolon in each element of the list

    Then, it will remove all trailing and leading whitespaces
    of the element of the list

    After that, it will return the cleaned version of the list
    '''

    for i in range(len(ls)):
        if (check_semicolon(ls[i])):
            ls[i] = ls[i].replace(";", "")
        ls[i] = ls[i].strip()
    return ls

def check_course(pre_ls, course_taken):
    '''
    This is to check if the student satisfy the
    prerequisite of the elective course based on
    the their course taken

    pre_ls: a list of prequisite course
    course taken: a list of course taken by the student

    The length of pre_ls indicate how many "AND" 
    requirement the students need to satisfy

    First, the function loop through each of 
    pre_ls element and split the element 
    by the occurence of "or" and assigned it to 
    variable pre_req_course

    After that, the function loop through pre_req_course
    to remove all whitespaces for each of its element

    After that, the function loop through the course taken
    and check if the course is in pre_req_course. As long as
    the course match one of the course in pre_req_course,
    the student has satisfy the first criteria.

    If there is a match, the True value is appended to 
    the condition variable 
    else the False value is appended instead

    After that, the functioon will check if the condition are met or 
    not.

    If there is a False value inside the condition, this means
    the student is ineligible to take the elective course.
    The function will return False as a result

    If there is no False value, then the student has met
    the criteria for the elective course and the function
    return True

    '''
    condition = []
    for or_course in pre_ls:
        found = False
        pre_req_course = or_course.split("or")
        for course in range(len(pre_req_course)):
            pre_req_course[course] = pre_req_course[course].strip()
        
        for c in course_taken:
            if c in pre_req_course:
                found = True
        condition.append(found)

    for result in condition:
        if result == False:
            return False
    
    return True


# File names variable
course_taken_filename = "csv-course-taken.csv"
course_i_can_take_filename = "csv-course-i-can-take.csv"
elective_filename = 'csv-comp-elective.csv'

# list to store course taken by student
my_course = []

with open(course_i_can_take_filename, 'w', newline='') as new_file:
    # Create or Reset the file that is to store the eligible course
    fieldnames=['Course Code', 'Course Name']
    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()

with open(course_taken_filename, newline='', encoding="utf-8") as course_file:
    # Retrieve the course taken by the student
    # and store it in my_course
    reader = csv.DictReader(course_file)
    for row in reader:
        my_course.append(row['Course Code'])


with open(elective_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Split the text into individual elements based on the occurence
        # of "AND"
        # The len of prereq indicates how many "AND" requirement there is
        # for the elective course
        prereq = clean_word(row['Prerequisite'].split("and"))
        if check_course(prereq, my_course):
            with open(course_i_can_take_filename, 'a', newline="") as write_file:
                # Open file in append mode and write the eligible course inside it
                fieldnames = ['Course Code', 'Course Name']
                writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                writer.writerow({'Course Code': row['Course Code'], 'Course Name': row['Course Name']})