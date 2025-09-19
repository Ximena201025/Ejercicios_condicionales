# Ejercicios Condicionales en Python

# Ejercicio 1
# Preguntar la edad y mostrar si es mayor de edad o no.
edad = int(input("¿Cuál es tu edad? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")


# Ejercicio 2
# Comparar contraseña sin importar mayúsculas/minúsculas.
contrasena_guardada = "contraseña"
contrasena_usuario = input("Introduce la contraseña: ")
if contrasena_guardada.lower() == contrasena_usuario.lower():
    print("La contraseña coincide.")
else:
    print("La contraseña no coincide.")


# Ejercicio 3
# Pedir dos números y mostrar su división, controlando división por cero.
num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce otro número: "))
if num2 != 0:
    print("La división es:", num1 / num2)
else:
    print("Error: No se puede dividir entre cero.")


# Ejercicio 4
# Pedir un número y decir si es par o impar.
numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


# Ejercicio 5
# Tributación según edad e ingresos.
edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuáles son tus ingresos mensuales? "))
if edad > 16 and ingresos >= 1000:
    print("Debes tributar.")
else:
    print("No debes tributar.")


# Ejercicio 6
# Asignar grupo según nombre y sexo.
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (Mujer/Hombre): ")
if (sexo.lower() == "mujer" and nombre.lower() < "m") or (sexo.lower() == "hombre" and nombre.lower() > "n"):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")


# Ejercicio 7
# Calcular tipo impositivo según renta anual.
renta = float(input("Introduce tu renta anual: "))
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
print(f"Tu tipo impositivo es {tipo}%.")


# Ejercicio 8
# Calcular rendimiento y dinero según puntuación.
puntos = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))
if puntos == 0.0:
    nivel = "Inaceptable"
elif puntos == 0.4:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None

if nivel:
    dinero = 2400 * puntos
    print(f"Tu nivel es {nivel} y recibirás {dinero}€.")
else:
    print("Puntuación no válida.")


# Ejercicio 9
# Precio de entrada según edad.
edad = int(input("Introduce tu edad: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10
print(f"El precio de la entrada es {precio}€.")


# Ejercicio 10
# Pizza vegetariana o no vegetariana.
print("¿Quieres una pizza vegetariana?")
opcion = input("Escribe 'si' o 'no': ").lower()

if opcion == "si":
    print("Ingredientes vegetarianos: Pimiento, Tofu")
    ingrediente = input("Elige un ingrediente: ")
    print(f"Pizza vegetariana con mozzarella, tomate y {ingrediente}.")
else:
    print("Ingredientes no vegetarianos: Peperoni, Jamón, Salmón")
    ingrediente = input("Elige un ingrediente: ")
    print(f"Pizza no vegetariana con mozzarella, tomate y {ingrediente}.")
