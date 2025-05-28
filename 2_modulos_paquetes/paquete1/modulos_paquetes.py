'''Un modulo es simplemente un archivo con eztension py que contiene
codigo phyton (fumciones,clases,variables,etx.).'''

import os

def tabladfor(num):
    for i in range (1,11): 
        multi=num*i
        regre=print((f"{num} x {i} = {multi}"))
        return regre

def tablaswhile():
    num=int(input("Dame un numero de la tabla de multiplicar: "))
    i=1
    while i<=10:
        multi=num*1
        print(f"{num} x {i} = {multi}")
        i+=1

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("...Oprima un tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"Hola bienvenido: {nom}!"

def solicitarDatos4():
    
    return
    
