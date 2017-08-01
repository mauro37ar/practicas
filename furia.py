#!/usr/bin/python


#datos personales:

nom_1=raw_input("ingrese nombre: ")

ape_1=raw_input("ingrese apellido: ")

dni_1= int(input("ingrese documento: "))

fecha_1=int(input ("fecha de ingreso: "))

nom_2= raw_input("ingrese nombre: ")

ape_2= raw_input("ingrese apellido: ")

dni_2= int(input("ingrese documento: "))

fecha_2=int(input ("fecha de ingreso: "))

nom_3= raw_input("ingrese nombre: ")

ape_3= raw_input("ingrese apellido: ")

dni_3= int(input("ingrese documento: "))

fecha_3=int(input ("fecha de ingreso: "))

#datos de materias y notas.

mate_1 = raw_input("ingrese materia: ")

nota_1 = input("ingrese nota: ")

nota_2 = input("ingrese nota: ")

nota_3 = input("ingrese nota: ")

mate_2 = raw_input("ingrese materia: ")

nota_4 = input("ingrese nota: ")

nota_5 = input("ingrese nota: ")

nota_6 = input("ingrese nota: ")

mate_3 = raw_input("ingrese materia: ")

nota_7 = input("ingrese nota: ")

nota_8 = input("ingrese nota: ")

nota_9 = input("ingrese nota: ")

mate_4 = raw_input("ingrese materia: ")

nota_10 = input("ingrese nota: ")

nota_11 = input("ingrese nota: ")

nota_12 = input("ingrese nota: ")

mate_5 = raw_input("ingrese materia: ")

nota_13 = input("ingrese nota: ")

nota_14  = input("ingrese nota: ")

nota_15 = input("ingrese nota: ")
#diccionarios.
per_1={"nombre" : nom_1, "apellido" : ape_1, "documento" : dni_1, "fecha de ingreso" : fecha_1}

per_2={"nombre" : nom_2, "apellido" : ape_2, "documento" : dni_2, "fecha de ingreso" : fecha_2}

per_3={"nombre" : nom_3, "apellido" : ape_3, "documento" : dni_3, "fecha de ingreso" : fecha_3}

mater_1={"materia" : mate_1, "aprobado" : "aprobado", "nota" : nota_1,"materia1" : mate_1, "aprobado1" : "aprobado", "nota1" : nota_2,"materia2" : mate_1, "aprobado2" : "aprobado", "nota2" : nota_3}

mater_2={"materia" : mate_2, "aprobado" : "aprobado", "nota" : nota_4,"materia1" : mate_2, "aprobado1" : "aprobado", "nota1" : nota_5,"materia2" : mate_2, "aprobado2" : "aprobado", "nota2" : nota_6}

mater_3={"materia" : mate_3, "aprobado" : "aprobado", "nota" : nota_7,"materia1" : mate_3, "aprobado1" : "aprobado", "nota1" : nota_8,"materia2" : mate_3, "aprobado2" : "aprobado", "nota2" : nota_9}

mater_4={"materia" : mate_4, "aprobado" : "aprobado", "nota" : nota_10,"materia1" : mate_4, "aprobado1" : "aprobado", "nota1" : nota_11,"materia2" : mate_4, "aprobado2" : "aprobado", "nota2" : nota_12}

mater_5={"materia" : mate_5, "aprobado" : "aprobado", "nota" : nota_13,"materia1" : mate_5, "aprobado1" : "aprobado", "nota1" : nota_14,"materia2" : mate_5, "aprobado2" : "aprobado", "nota2" : nota_15}

#listas.

alumnos=[per_1, per_2, per_3]

materias=[mater_1, mater_2, mater_3, mater_4, mater_5]

print materias , alumnos

#funcion para temer lista del alumno con su materia y notas.

def alumno_nuevo(alumnos):

    for dato in alumnos:

        dato = input("ingrese documento a buscar: ")
                      
        if dni_1 == dato:
           
            alumno_1 = [nom_1, ape_1, mate_1, nota_1, mate_2, nota_4, mate_3, nota_7, mate_4, nota_10, mate_5, nota_13]

            return alumno_1

        elif dni_2 == dato:

            alumno_2=[nom_2, ape_2, mate_1, nota_2, mate_2, nota_5, mate_3, nota_8, mate_4, nota_11, mate_5, nota_14]

            return alumno_2
              
        else:

            alumno_3 = [nom_3, ape_3, mate_1, nota_3, mate_2, nota_6, mate_3, nota_9, mate_4, nota_12, mate_5, nota_15]

            return alumno_3
        
# funcion para llegar al promedio por alumnos.

#imprime una lista con el apellido, nombre y promedio buscado

def prom_alumnos(alumnos):

    for ape in (alumnos):

        ape=raw_input ("ingrese apellido:")

        for  nombre in (alumnos):

             nom=raw_input ("ingrese nombre: ")
               
             if ape == ape_1 and nom == nom_1:

                prom=(nota_1+nota_4+nota_7+nota_10+nota_13)/5

                promedio_1=int(prom)

                alumno_4=[ape_1, nom_1, promedio_1]
            
                return alumno_4

             if ape == ape_2 and nom == nom_2:

                prom=(nota_2+nota_5+nota_8+nota_11+nota_14)/5

                promedio_2=int(prom)

                alumno_5=[ape_2, nom_2, promedio_2]
            
                return alumno_5

             else:

                  prom=(nota_3+nota_6+nota_10+nota_13+nota_15)/5

                  promedio_3=int(prom)

                  alumno_6=[ape_3, nom_3, promedio_3]

                  return  alumno_6



    
print alumno_nuevo(alumnos)
print prom_alumnos(alumnos)
    
 
