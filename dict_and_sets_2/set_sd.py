morning_set = {"Java", "C", 'Ruby', "Lisp", 'C#'}
afternoon_set = {'Python', 'C#', 'Java', 'C', 'Ruby'}

# doing the same with lists.
morning_list = ["Java", "C", 'Ruby', "Lisp", 'C#']
afternoon_list = ['Python', 'C#', 'Java', 'C', 'Ruby']

# the set version
possible_courses = morning_set ^ afternoon_set
print(possible_courses)

# if you have list you can use the set() to convert to set and do the operation.
possible_courses = set(afternoon_list).symmetric_difference(morning_list)
print(possible_courses)
