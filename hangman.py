import random
import time

print('Bienvenido a Hangman')

jugador_1 = input('Ingresa tu nombre jugador 1: ')

print(
  'Primero', jugador_1,
  'adivinaras una palabra letra por letra y luego, el que acierte la palabra en menos fallos gana.'
)
time.sleep(0.5)
print('\nTendran 7 vidas por lo que si tienen 7 letras mal pierden')

DIBUJO = [
  '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

palabras = [
  'SANGRE', 'NEGOCIO', 'PUBLICIDAD', 'BUENA', 'ROEDOR', 'LEON', 'JIRAFA',
  'FUTBOL', 'COLEGIO', 'AUTO', 'CAMION', 'MADERA', 'ARBOL', 'AMIGOS', 'CERRO',
  'COMPUTADOR', 'FLORES', 'PELOTA', 'JUICIO', 'GUARDIA', 'WHATSAPP',
  'INSTAGRAM', 'DISCORD', 'AMAZON', 'PROFESOR', 'CABEZA', 'CUERPO', 'MANOS',
  'FOTOS', 'VIDEOS', 'CARGADOR', 'YOUTUBE', 'CARPETA', 'CELULAR', 'RELOJ',
  'PERRO', 'GATO', 'SOL', 'LUNA', 'ESPACIO', 'AUDIFONOS', 'ELEFANTE',
  'HIPOPOTAMO', 'PISCINA', 'PASTO', 'TIERRA', 'AGUA', 'ELECTRICIDAD',
  'ENOJADO', 'FELIZ', 'TRISTE', 'VENTILADOR', 'DEPREDADOR',
  'OTORRINOLARINGOLOGO'
]

max_malas = len(DIBUJO) - 1

palabra_jugador_1 = random.choice(palabras)

actual_adivinanza_1 = '-' * len(palabra_jugador_1)

fallos_1 = 0
vidas_1 = 7
letras_ocupadas_1 = []

while fallos_1 < max_malas and actual_adivinanza_1 != palabra_jugador_1:
  print(DIBUJO[fallos_1])
  print(jugador_1, 'Haz usado las siguientes letras:', letras_ocupadas_1)
  print(jugador_1, 'Hasta ahora tu palabra es:', actual_adivinanza_1)

  adivinar_1 = input('\nAdivina una letra:')
  adivinar_1 = adivinar_1.upper()

  time.sleep(1)

  while adivinar_1 in letras_ocupadas_1:
    print('Ya haz usado esta letra', adivinar_1)
    adivinar_1 = input('Prueba con otra letra:')
    adivinar_1 = adivinar_1.upper()

  letras_ocupadas_1.append(adivinar_1)

  if adivinar_1 in palabra_jugador_1:
    print('\nHaz adivinado bien')

  else:
    print('\n', jugador_1, 'Estas incorrecto :(')
    fallos_1 += 1

  nueva_actual_adivinanza_1 = ''
  for letra_1 in range(len(palabra_jugador_1)):
    if adivinar_1 == palabra_jugador_1[letra_1]:
      nueva_actual_adivinanza_1 += adivinar_1
    else:
      nueva_actual_adivinanza_1 += actual_adivinanza_1[letra_1]

  actual_adivinanza_1 = nueva_actual_adivinanza_1

if fallos_1 == max_malas:
  print(DIBUJO[fallos_1])
  print('HAZ PERDIDO', jugador_1)
  print('La palabra correcta era', palabra_jugador_1)

else:
  (jugador_1, 'Haz ganado')
