def sumaentreposiciones(lst, pi, pf):
    if pi > pf:
        return 0
    else:
        return lst[pi-1] + sumaentreposiciones(lst, pi+1, pf)

txtlista = input("Ingrese los números de la lista separados por espacios: ")
lista = [int(num) for num in txtlista.split()]

PI = int(input("Ingrese la posición inicial: "))
PF = int(input("Ingrese la posición final: "))

resultado = sumaentreposiciones(lista, PI, PF)
print(f"\nLista ingresada: {lista}")
print(f"Resultado = {resultado}")