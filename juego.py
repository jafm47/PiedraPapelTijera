
import random

# Método para validar la entrada del Usuario.
def validar_entrada(entrada):
    global valor
    encontrado=False
    for clave,valor in lista_Opciones_Usuario.items():
        if clave==entrada:
            encontrado=True
            valor = lista_Opciones_Usuario[clave]
            break
    return encontrado

# Método que comprueba la jugada.
def comprobar_jugada(entrada):
    if entrada==0 and numero_aleatorio==0:
        print(f"Has elegido {valor} y {valor} empata con {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==0 and numero_aleatorio==1:
        print(f"Has elegido {valor} y {valor} pierde con {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==0 and numero_aleatorio==2:
        print(f"Has elegido {valor} y {valor} gana a {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==1 and numero_aleatorio==0:
        print(f"Has elegido {valor} y {valor} gana a {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==1 and numero_aleatorio==1:
        print(f"Has elegido {valor} y {valor} empata con {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==1 and numero_aleatorio==2:
        print(f"Has elegido {valor} y {valor} pierde con {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==2 and numero_aleatorio==0:
        print(f"Has elegido {valor} y {valor} pierde con {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==2 and numero_aleatorio==1:
        print(f"Has elegido {valor} y {valor} gana a {lista_Opciones_IA[numero_aleatorio]}")
    elif entrada==2 and numero_aleatorio==2:
        print(f"Has elegido {valor} y {valor} empata con {lista_Opciones_IA[numero_aleatorio]}")
    else:
        print(f"Has elegido {valor} y la jugada no es valida")


# Diccionario con los datos de entrada del usuario.
lista_Opciones_Usuario = {
    0: 'Piedra',
    1: 'Papel',
    2: 'Tijera'
}

#  Lista con los datos de IA
lista_Opciones_IA=["Piedra","Papel","Tijera"]

# Genera un numero aleatorio entre 0 y 2
numero_aleatorio=random.randint(0,2)

# Entrada del usuario
entrada=input("Introduce un numero [0:Piedra,1:Papel,2:Tijera]: ")

# Convierte a un numero entero la entrada del usuario
try:
    entrada=int(entrada)
except:
    print("Introduce un numero valido")
    exit()

# Valida la entrada del usuario
entrada_valida = validar_entrada(entrada)
if entrada_valida:
    # Valida la jugada con la entrada del usuario.
    comprobar_jugada(entrada)
else:
    print("No has introducido una opción valida")



