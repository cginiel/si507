
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


max = 0
max_id = -1
for id in grades: # loop through each student (by using their ID). This iterates through our keys in the dictionary. ID will be assigned to each key as you loop.
    sum = 0 # since we're about to do arithmetic in a loop, we set up temp variable and start our values at zero
    num_grades = 0
    for g in grades[id]: # loop through the posted grades
        sum += g # sum of all scores
        num_grades += 1 # sum of how may grades posted (in this case, all students have 4 grades)
    avg = sum/num_grades # find the average grade for each ID
    if avg > max: # means: is this average greater than the max we've seen so far?
        max = avg # new greatest average
        max_id = id # assign max_id to highest average and assign that to student's ID
print(students[max_id])