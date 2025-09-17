# Ejercicio 1
nombre = input("Introduce tu nombre: ")
numero = int(input("Introduce un número entero: "))
for i in range(numero):
    print(nombre)


# Ejercicio 2
nombre_completo = input("Introduce tu nombre completo: ")
print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title())


# Ejercicio 3
nombre = input("Introduce tu nombre: ")
print(f"{nombre.upper()} tiene {len(nombre)} letras")


# Ejercicio 4
telefono = input("Introduce un número de teléfono en formato +34-XXXXXXXXX-XX: ")
print("Número sin prefijo ni extensión:", telefono[4:-3])


# Ejercicio 6
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")
print(frase.replace(vocal, vocal.upper()))


# Ejercicio 7
email = input("Introduce tu correo electrónico: ")
nombre_usuario = email.split('@')[0]
print(nombre_usuario + "@ceu.es")


# Ejercicio 8
precio = input("Introduce el precio en euros con dos decimales (ej: 34.56): ")
euros, centimos = precio.split(".")
print(f"Euros: {euros} - Céntimos: {centimos}")


# Ejercicio 9
fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
dia, mes, año = fecha.split("/")
print("Día:", dia)
print("Mes:", mes)
print("Año:", año)


# Ejercicio 10
productos = input("Introduce los productos de la cesta separados por comas: ")
for producto in productos.split(","):
    print(producto.strip())


# Ejercicio 11
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))
print("{:s} {:09.2f} {:03d} {:011.2f}".format(producto, precio, unidades, precio*unidades))
