# while True:
#     response = input("What say you? ")
#     if (response.isnumeric()):
#         response = int(response)
#         if (response > 3 and response < 5):
#             break
#         else:
#             print('hello' * response)
#     else:
#         print("You say", response, "????")
# print("goodbye")  

# def refruit(d):
#     d['g'] = 'grapefruit'
#     d['a'] = 'apple'
#     d = {'g': 'guava', 'c': 'cherry', 'a': 'apricot'}

# fruits = {'g': 'grape', 'p': 'plum', 'o': 'orange'}
# refruit(fruits)
# print(fruits['g'])
# print(fruits['a'])
# print(fruits['p'])

# print('boyz2men'.isalpha())

# import copy

# students = {
#     '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
#     '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
#     '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
#     '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
# }

# grades = {
#     '1001': [90, 88, 75, 95],   
#     '1002': [92, 99, 88, 100],
#     '1003': [95, 88, 82, 100],
#     '1004': [99, 92, 94, 98]
# }


# def do_grades(grades):
#     for id in grades:
#         sum = 0
#         num_items = 0
#         for n in grades[id]:
#             sum += n
#             num_items += 1
#         students[id]["average"] = sum/num_items
# #### the chunk above calculates average grades and creates a new dictionary key/value pair for them ####
    
#     student_grades = {}
#     for id in grades:
#         sum = 0
#         num_items = 0
#         for n in grades[id]:
#             sum += n
#             num_items += 1
#         student_grades[id] = sum/num_items
# #### this nearly performs the same task as the code above except instead of adding a new dict entry it just sets each id equal to the average grade ####
    
#     for id in student_grades:
#         student = students[id]
#         print(student['first_name'], 
#             student['last_name'], 'has', 
#             student_grades[id])

# do_grades(grades)


students = {
    '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
    '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
    '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
    '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
}

grades = {
    '1001': [90, 88, 75, 95],   
    '1002': [92, 99, 88, 100],
    '1003': [95, 88, 82, 100],
    '1004': [99, 92, 94, 98]
}

def calculate_student_averages(students, grades):
    '''calculate and keep each student's average
        takes a dictionary of students and a dictionary of grades,  
        calculates averages for each student, then adds the average
        to the student's record in the students dictionary.
        Parameters
        ----------
        students : dict
            student info, indexed by id {id: {student_info}}
            modified in place by adding each student's average 
            to their record (key = 'average') 
            
        grades : dict
            student grades, indexed by id {id: [list_of_grades]}
        Returns
        -------
        list
            the list of students, modified to include each student's 
            average grade
    '''

    for id in grades:
        sum = 0
        num_items = 0
        for n in grades[id]:
            sum += n
            num_items += 1
        students[id]["average"] = sum/num_items

calculate_student_averages(students, grades)
print(students)