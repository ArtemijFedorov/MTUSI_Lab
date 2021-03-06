groupmates = [ 
 { 
 "name": "Алина", 
 "surname": "Самитина", 
 "exams": ["Информатика", "ЭЭиС", "Web"], 
 "marks": [4, 3, 5] 
 }, 
 { 
 "name": "Василий", 
 "surname": "Сасс", 
 "exams": ["История", "ЭЭиС", "КТП"], 
 "marks": [4, 4, 4] 
 }, 
 { 
 "name": "Айк", 
 "surname": "Саядян", 
 "exams": ["Философия", "Web", "ЭЭиС"], 
 "marks": [5, 5, 4] 
 }, 
 { 
 "name": "Акоп", 
 "surname": "Саядян", 
 "exams": ["Матан", "ИС", "КТП"], 
 "marks": [5, 4, 5] 
 }, 
 { 
 "name": "Александр", 
 "surname": "Солонин", 
 "exams": ["Философия", "История", "Физика"], 
 "marks": [4, 5, 5] 
 }
]

def print_students(students): 
 print(u"Имя".ljust(15), u"Фамилия".ljust(10),  u"Экзамены".ljust(30), u"Оценки".ljust(20)) 
 for student in students:
     print(student["name"].ljust(15),  
student["surname"].ljust(10), str(student["exams"]).ljust(30),  str(student["marks"]).ljust(20)) 
print_students(groupmates) 
