# Ejercicio con dos listas
def contar(strings, queries):
    result = []
    for q in queries:
        contador = 0
        for s in strings:
            if q == s:
                contador += 1
        result.append(contador)
    return (result)


qr = ['ab', 'bc', 'abc']
st = ['ab', 'ab', 'abc']
print(contar(st, qr))

# Buscar el unico elemento en una lista

a = [0, 0, 1, 2, 1]
lista = []


def lonelyinteger(a):
    lista = []
    for indice, valor in enumerate(a):
        if valor in lista:
            continue
        else:
            b = a[indice+1:]
            if valor in b:
                lista.append(valor)

    for valor in a:
        if valor not in lista:
            return (valor)


print(lonelyinteger(a))

# Cambiar un numero a base dos luego conbertirlo a 32 bits, cambiar los 0 por 1 y regresar ese numero a base 10
# 1 Pasar el numero a base 2
n = 4
contador = 0
numero = ""
while n > 0:
    contador += 1
    a = divmod(n, 2)
    n = a[0]
    numero = str(a[1])+numero
print(numero)
# 2 Convertir los 0 en 1 y al reves
# esto si funciona pero quise realizar esta opcion en una lista de comprension
'''alreves = ""
for elemento in numero:
    if elemento == "0":
        a = 1
    else:
        a = 0
    alreves = str(alreves)+str(a)'''
alreves = "".join(['1' if elemento == '0' else '0' for elemento in numero])
print(alreves)

# 3 Agregarle los unos para que sea de longitud 32

unos = (32-contador)*"1"+alreves

# convertir los numeros a base 10
print(int(unos, 2))
