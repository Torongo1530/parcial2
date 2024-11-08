
numeros = []

while True:

    def sumaAcumulativa (numero):
        numeros.append(numero)
        print(sum(numeros))

    sumaAcumulativa(int(input("Ingrese un numero: ")))
