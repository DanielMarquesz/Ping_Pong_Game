import turtle
import winsound

# Criacao da tela
wn = turtle.Screen()
wn.title('Ping Pong by Daniel Marques')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Pontos
pontos_1 = 0
pontos_2 = 0

# Raquete esquerda
raquete_e = turtle.Turtle()
raquete_e.speed(0)
raquete_e.shape('square')
raquete_e.color('white')
raquete_e.shapesize(stretch_wid=5, stretch_len=1)
raquete_e.penup()
raquete_e.goto(-350, 0)

# Raquete direita
raquete_d = turtle.Turtle()
raquete_d.speed(0)
raquete_d.shape('square')
raquete_d.color('white')
raquete_d.shapesize(stretch_wid=5, stretch_len=1)
raquete_d.penup()
raquete_d.goto(350, 0)

# Texto
texto = turtle.Turtle() # Instância o módulo Turtle
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write('Jogardor 1: 0 | Jogador 2: 0',align='center', font=('Courier', 24, 'bold'))

# Funcoes
def raquete_e_up(): # Raquete esquerda para cima
    y = raquete_e.ycor()
    y += 25
    raquete_e.sety(y)

def raquete_e_down(): # Raquete esquerda para baixo
    y = raquete_e.ycor()
    y -= 25
    raquete_e.sety(y)

    # Raquete Direita

def raquete_d_up(): # Raquete direita para cima
    y = raquete_d.ycor()
    y += 25
    raquete_d.sety(y)

def raquete_d_down(): # Raquete direita para baixo
    y = raquete_d.ycor()
    y -= 25
    raquete_d.sety(y)


# Config Keyboard
wn.listen()
wn.onkeypress(raquete_e_up, 'w')
wn.onkeypress(raquete_e_down, 's')
wn.onkeypress(raquete_d_up, 'Up')
wn.onkeypress(raquete_d_down, 'Down')

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color('white')
bola.penup()
bola.goto(0, 0) # Ponto inicial
bola.dx = 0.6 # Direção e velocidade da bola horizontalmente
bola.dy = -0.6 # Direção e velocidade da bola horizontalmente

# Main Game Loop
while True:
    wn.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Borda Superior e Inferior
    if bola.ycor() > 290: # -10px referentes a bola, pois bottom e top possuem 300px cada
        bola.sety(290)
        bola.dy *= -1 # Se a coordenada Y for maior que a borda, a bola vai na direção oposta
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC) # O Jogo sem som é bem melhor

    if bola.ycor() < -290: # -10px referentes a bola, pois bottom e top possuem 300px cada
        bola.sety(-290)
        bola.dy *= -1 # Se a coordenada Y for maior que a borda, a bola vai na direção oposta
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    # Borda Esquerda e Direita
    if bola.xcor() > 390: # Se a bola ultrapassar a borda direita, ela retorna ao centro na direção oposta
        bola.goto(0, 0) # Retorna ao centro
        bola.dx *= -1 # Inverte a direção multiplicando por -1
        texto.clear() # Apaga o placar anterior
        pontos_2 += 1
        texto.write('Jogardor 1: {} | Jogador 2: {}'.format(pontos_2,pontos_1),align='center', font=('Courier', 24, 'bold'))


    if bola.xcor() < -390: # Se a bola ultrapassar a borda esquerda, ela retorna ao centro na direção oposta
        bola.goto(0, 0) # Retorna ao centro
        bola.dx *= -1 # Inverte a direção multiplicando por -1
        texto.clear() # Apaga o placar anterior
        pontos_1 += 1
        texto.write('Jogardor 1: {} | Jogador 2: {}'.format(pontos_2,pontos_1),align='center', font=('Courier', 24, 'bold'))


    # Rebatimento das Raquetes
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_d.ycor() +40 and bola.ycor() > raquete_d.ycor() -40):
        bola.setx(340)
        bola.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_e.ycor() +40 and bola.ycor() > raquete_e.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
