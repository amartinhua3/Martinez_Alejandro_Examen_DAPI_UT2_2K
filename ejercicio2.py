alumno = {'nombre':' ', 'calificado' : ''}
alumno2 = {'nombre2' : '', 'calificado2' : ''}
for alumnos in alumno:
    alumno['nombre'] = input('Introduce el nombre del alumno: ')
    alumno['calificado'] = input('Escriba si está aprobado o suspendido: ')

    alumno2['nombre2'] = input('Introduce el nombre del alumno: ')
    alumno2['calificado2'] = input('Escriba si está aprobado o suspendido: ')
alumno.update(alumno2)
n_aprobados = input('Introduzca el número de aprobados: ')
print('El número de aprobados es: ', n_aprobados)

print(alumno.values())