import math
from turtle import *

speed(0)
color("black")

C1 = None
C2 = None

def dibujar_linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    

    ultima_posicion = [x2,y2]

    return ultima_posicion
#calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

def cara_1(x,y,t):
    global C1
    vertice_frontal(x,y,t)
    dibujar_linea(C1[0][0],C1[0][1],C1[1][0],C1[1][1])
    dibujar_linea(C1[1][0],C1[1][1],C1[2][0],C1[2][1])
    dibujar_linea(C1[2][0],C1[2][1],C1[3][0],C1[3][1])
    dibujar_linea(C1[3][0],C1[3][1],C1[0][0],C1[0][1])
def cara_2(x,y,t):
    global C2
    vertice_techo(x,y,t)
    dibujar_linea(C2[0][0],C2[0][1],C2[1][0],C2[1][1])
    dibujar_linea(C2[1][0],C2[1][1],C2[2][0],C2[2][1])
    dibujar_linea(C2[2][0],C2[2][1],C2[3][0],C2[3][1])
    dibujar_linea(C2[3][0],C2[3][1],C2[0][0],C2[0][1])

def diagonales(C1,C2):
    for i in range(0,4):
        dibujar_linea(C1[i][0],C1[i][1],C2[i][0],C2[i][1])

def vertice_frontal(x,y,t):
    global C1
    C1 = [
        [x+t/2,y+t/2],#veritce 1
        [x+t/2,y-t/2],#vertice 2
        [x-t/2,y-t/2],#veritce 3
        [x-t/2,y+t/2]#vertice 4
    ]
def vertice_techo(x,y,t):
        global C2
        C2 = [
        [x+t/2,y+t/2],#veritce 1
        [x+t/2,y-t/2],#vertice 2
        [x-t/2,y-t/2],#veritce 3
        [x-t/2,y+t/2]#vertice 4
    ]

x,y,t = 40,40,150

cara_1(x,y,t)
cara_2(x+t/2,y+t/2,t)
diagonales(C1,C2)

done()