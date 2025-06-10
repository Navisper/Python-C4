#Pide el número de estudiantes en tres cursos y muestra el promedio de estudiantes por curso. 

estudiantes_curso1 = int(input("Please enter the number of students in the course 1"))
estudiantes_curso2 = int(input("Please enter the number of students in the course 2"))
estudiantes_curso3 = int(input("Please enter the number of students in the course 3"))


promedio_cursos = (estudiantes_curso1 + estudiantes_curso2 + estudiantes_curso3)/3

print(f"the average number of students per course is of {promedio_cursos:.2f} students")