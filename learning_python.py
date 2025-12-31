message = 'hello'
print(message[0:3])
greeting = "hello"
name = "John"

new = f'{greeting}, {name}, Welcom!'
print(new)

#lists
courses = ['History', 'Math', 'Physics']
print(courses)
courses.append('Art')
print(courses)
courses.insert(1, 'Lectuture')
print(courses)
courses.sort()
print(courses)

for course in courses:
    print(course)
    
for (index, course) in enumerate(courses):
    print (index, course)
    
for (index, course) in enumerate(courses, start=1):
    print (index, course)    

course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)
