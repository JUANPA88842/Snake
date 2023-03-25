import turtle
import time
import random
from collections import deque

#1.0 Variables iniciales

#Marcador
score = 0
highscore = 0


#Variables
posponer = 0.1
coordenadas = deque()
pi = deque()


#Boton para iniciar p
def Iniciar():
    pi.append(0)


#Configuración de la ventana
ventana=turtle.Screen()
ventana.title("Culebra Manzanera")
ventana.bgcolor("white")
ventana.setup(width=300, height=300)
ventana.tracer(0)       #Animación más amigable a nuestros ojos


#Cabeza de la serpiente
cabeza = turtle.Turtle()    #Crea la cabeza
cabeza.speed(0)     #Cuando se inicia la pantalla el cuadrado ya está ahí
cabeza.shape("square")
cabeza.color("#484a50")
cabeza.penup()      #No deja rastro cuando se mueve la cabeza
cabeza.goto(0,0)    #Posicion en el centro
cabeza.direction = "stop"   #No se mueve aún cuando aparece en pantalla


#Partes del cuerpo
cuerpo1 = turtle.Turtle()    
cuerpo1.speed(0)     
cuerpo1.shape("square")
cuerpo1.color("grey")
cuerpo1.penup()
cuerpo1.direction = "stop"
cuerpo1.goto(0,-20)    


cuerpo2 = turtle.Turtle()    
cuerpo2.speed(0)     
cuerpo2.shape("square")
cuerpo2.color("grey")
cuerpo2.penup()
cuerpo2.direction = "stop"
cuerpo2.goto(0,-40) 


cuerpos = deque()
cuerpos.append(cuerpo1)
cuerpos.append(cuerpo2)


#Tortuga ó manzana
comida = turtle.Turtle() 
comida.speed(0)   
comida.shape("turtle")
comida.color("red")
comida.penup()  
comida.goto(60,60)    


#Cuerpo serpiente
segmentos = deque()


#Texto
texto = turtle.Turtle()
texto.speed(1)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,110)
texto.write("Score: 0    high Score: 0", align = "center", font=("Courier",11, "normal"))

#2.0 Inicio del programa

def inicio():
    """Pantalla inicial del juego
    """
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("black")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,0)
    texto.write("Snake \n El videojuego \n Presiona /P/ para empezar", align = "center", font=("Comic Sans MS",12, "italic"))
    texto.clear()


def reglas():
    """Reglas
    """
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("black")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,-90)
    texto.write("Movimiento : A W S D \n 1: No puedes chocarte con \n Tu propio cuerpo \n \n 2: No puedes chocarte con el borde \n \n 3: Come manzanas como si tu \n tu vida dependiera de ello. \n \n /P/ Para iniciar el juego ", align = "center", font=("Comic Sans MS",10, "italic"))
    texto.clear()

#3.0 Textos que aparecen al perder

def TextoFinal():
    """Función que se ejecuta cunado se choca la serpiente
    """
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("red")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,0)
    texto.write("Te chocaste \n", align = "center", font=("Comic Sans MS",25, "italic"))
    texto.clear()


def MovimientoIncorrecto():
    """Función que se ejecuta cuando la persona oprime un movimeinto incorrecto \n como ir en contra de la dirección de la serpiente
    """
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("red")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,0)
    texto.write("Movimiento \n incorrecto", align = "center", font=("Comic Sans MS",25, "italic"))
    texto.clear()


def Chocaste():
    """Función que se ejecuta cuando la serpiente se come a sí misma
    """
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("red")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,0)
    texto.write("Te comiste", align = "center", font=("Comic Sans MS",25, "italic"))
    texto.clear()


#4.0 Funciones de movimiento para la cabeza

def Arriba():
    cabeza.direction="up"

def Abajo():
    cabeza.direction="down"

def Izquierda():
    cabeza.direction="left"

def Derecha():
    cabeza.direction="right"


def mov():
    """Función de movimiento que indica cuantos píxeles y hacia donde se debe mover la cabeza según la dirección
    """
    if cabeza.direction=="up":
        y = cabeza.ycor()  
        cabeza.sety(y+20)  
    elif cabeza.direction=="down":
            y = cabeza.ycor()   
            cabeza.sety(y-20)         
    elif cabeza.direction=="left":
            x = cabeza.xcor()   
            cabeza.setx(x-20)   
    elif cabeza.direction=="right":
            x = cabeza.xcor()   
            cabeza.setx(x+20)
   

#Teclado
ventana.listen()  #Pantalla atenta a los eventos del teclado
ventana.onkeypress(Arriba, "w")
ventana.onkeypress(Abajo, "s")
ventana.onkeypress(Izquierda, "a")
ventana.onkeypress(Derecha, "d")
ventana.onkeypress(Iniciar, "p")


#Elementos iniciales
coordenadas.append([cabeza.xcor(),cabeza.ycor()])
coordenadas.append([cuerpo1.xcor(),cuerpo1.ycor()])
coordenadas.append([cuerpo2.xcor(),cuerpo2.ycor()])
contador = 0


#5.0 Bucle infinito del juego

while True:
    """Ejecuta las pantallas de inicio, reglas y el jeugo principal. \n Se establecen la lógica de funcionamiento para todos los casos, comer manzana, colisionar,posicionar manzana, aumentar marcador, y crecer el cuerpo de la serpiente.
    """
    if len(pi) == 0:
        final = inicio()
        time.sleep(1)
    elif len(pi) == 1:
        final = reglas()
        time.sleep(1)
    elif len(pi) > 1:
        ventana.update()  
        coordenadas.insert(0,[cabeza.xcor(),cabeza.ycor()])
        coordenadas.pop()
        contador += 1
        time.sleep(posponer) 
        #Colisiones por choque con paredes
        if cabeza.xcor()> 120 or cabeza.xcor() < -120 or cabeza.ycor() > 120 or cabeza.ycor() < -120:
            final = TextoFinal()
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            cuerpo1.goto(0,-20)
            cuerpo2.goto(0,-40)
            cuerpo1.direction = "stop"
            cuerpo2.direction = "stop"
            comida.goto(60,60)
            #desaparecer segmentos
            for j in segmentos:
                j.goto(1000,1000)
            #Condiciones iniciales
            segmentos=deque()
            coordenadas=deque()
            score = 0
            texto.clear()
            texto.write("Score: {}    High Score: {}".format(score, highscore), align = "center", font=("Courier",11, "normal"))
            coordenadas.append([cabeza.xcor(),cabeza.ycor()])
            coordenadas.append([cuerpo1.xcor(),cuerpo1.ycor()])
            coordenadas.append([cuerpo2.xcor(),cuerpo2.ycor()])
            contador = 0
        movimientomanz = 25
        #Mover la manzana de sitio si no es comida
        if contador == movimientomanz:
            xant = comida.xcor()
            yant = comida.ycor()
            x = random.randrange(-100,100,20)
            y = random.randrange(-100,100,20)
            while True:
                if [x,y] in coordenadas:
                    x = random.randrange(-100,100,20)
                    y = random.randrange(-100,100,20)
                    xc = cabeza.xcor()
                    yc = cabeza.ycor()
                    if x == xc+20 or x == xc-20 or x == yc+20 or x == xc-20:  
                        x = random.randrange(-100,100,20)
                        y = random.randrange(-100,100,20)
                        continue
                    continue
                elif [x,y] == [xant,yant]:
                    x = random.randrange(-100,100,20)
                    y = random.randrange(-100,100,20)
                    continue
                else:
                    xant = x
                    yant = y
                    break
            comida.goto(x,y)   
            contador=0
        #Comer mazana
        if cabeza.distance(comida) < 20:
            xant = comida.xcor()
            yant = comida.ycor()
            x = random.randrange(-100,100,20)
            y = random.randrange(-100,100,20)
            while True:
                if [x,y] in coordenadas:
                    x = random.randrange(-100,100,20)
                    y = random.randrange(-100,100,20)
                    xc = cabeza.xcor()
                    yc = cabeza.ycor()
                    if x == xc+20 or x == xc-20 or x == yc+20 or x == xc-20:
                        x = random.randrange(-100,100,20)
                        y = random.randrange(-100,100,20)
                        continue
                    continue
                elif [x,y] == [xant,yant]:
                    x = random.randrange(-100,100,20)
                    y = random.randrange(-100,100,20)
                    continue
                else:
                    xant = x
                    yant = y
                    break
            comida.goto(x,y)   
            contador=0
            #Crear segmento nuevo
            nuevo_segmento = turtle.Turtle() 
            nuevo_segmento.speed(0)   
            nuevo_segmento.shape("square")
            nuevo_segmento.color("grey")
            nuevo_segmento.penup()  
            segmentos.append(nuevo_segmento)
            coordenadas.append([segmentos[-1].xcor(),segmentos[-1].ycor])
            #Actualizar Score
            score += 1
            if score > highscore:
                highscore = score
            texto.clear()
            texto.write("Score: {}    High Score: {}".format(score, highscore), align = "center", font=("Courier",11, "normal"))
        totalSeg = len(segmentos)
        for i in range(totalSeg -1, 0, -1):
            x = segmentos[i-1].xcor()
            y = segmentos[i-1].ycor()
            segmentos[i].goto(x,y) 
        if totalSeg > 0:
            x = cuerpo2.xcor()
            y = cuerpo2.ycor()
            segmentos[0].goto(x,y)
        #Mover cuerpo del inicio
        if cabeza.direction != "stop":
                for i in range(len(cuerpos) -1, 0, -1):
                    x = cuerpos[i-1].xcor()
                    y = cuerpos[i-1].ycor()
                    cuerpos[i].goto(x,y)
                    x = cabeza.xcor()
                    y = cabeza.ycor()
                    cuerpos[0].goto(x,y)
        mov()
        #Colisiones con cuerpo
        for i in segmentos:
            if i.distance(cabeza) < 20:
                final = Chocaste()
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction = "stop"
                cuerpo1.goto(0,-20)
                cuerpo1.direction = "stop"
                cuerpo2.goto(0,-40)
                cuerpo2.direction = "stop"
                comida.goto(60,60)
                coordenadas=deque()
                #Esconder segmentos
                for i in segmentos:
                    i.goto(1000,1000)
                segmentos=deque()
                #resetear marcador
                score = 0
                texto.clear()
                texto.write("Score: {}    High Score: {}".format(score, highscore), align = "center", font=("Courier",11, "normal"))
                #Operaciones re retorno a estado inicial
                coordenadas.append([cabeza.xcor(),cabeza.ycor()])
                coordenadas.append([cuerpo1.xcor(),cuerpo1.ycor()])
                coordenadas.append([cuerpo2.xcor(),cuerpo2.ycor()])
                contador = 0
        for i in cuerpos:
            if i.distance(cabeza) < 19:
                final = MovimientoIncorrecto()
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction = "stop"
                cuerpo1.goto(0,-20)
                cuerpo1.direction = "stop"
                cuerpo2.goto(0,-40)
                cuerpo2.direction = "stop"
                comida.goto(60,60)
                #Esconder segmentos
                for i in segmentos:
                    i.goto(1000,1000)
                segmentos.clear()
                coordenadas=deque()
                #Resetear marcador
                score = 0
                texto.clear()
                texto.write("Score: {}    High Score: {}".format(score, highscore), align = "center", font=("Courier",11, "normal"))
                #Operaciones de retorno a estado inicial
                coordenadas.append([cabeza.xcor(),cabeza.ycor()])
                coordenadas.append([cuerpo1.xcor(),cuerpo1.ycor()])
                coordenadas.append([cuerpo2.xcor(),cuerpo2.ycor()])
                contador = 0

