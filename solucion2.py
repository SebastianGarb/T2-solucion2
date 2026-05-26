def suma_entre_posiciones(lst, pi, pf):
    if pi > pf:
        return 0
    else:
        return lst[pi-1] + suma_entre_posiciones(lst, pi+1, pf)

texto_lista = input("Ingrese los números de la lista separados por espacios: ")
lista = [int(num) for num in texto_lista.split()]

PI = int(input("Ingrese la posición inicial: "))
PF = int(input("Ingrese la posición final: "))

resultado = suma_entre_posiciones(lista, PI, PF)
print(f"\nLista ingresada: {lista}")
print(f"Resultado = {resultado}")