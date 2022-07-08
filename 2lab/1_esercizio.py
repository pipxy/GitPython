## Write a program that reads from input a given number of positive integers,
## till user press -1. Then the program will print sum, average, max, min

lista_N = []
nuovo_n = int(input("Inserisci un numero intero "))

while nuovo_n != -1:
    lista_N.append(nuovo_n)
    print("Ecco la nuova lista: ", lista_N)
    nuovo_n = int(input("Inserisci un numero intero "))
else:
    print()
    print()
    print()
    print("ERROR 404, hai inserito -1 !!!")
    print()
    print("La somma dei numeri inseriti è: ", sum(lista_N))
    print("La media  dei numeri inseriti è: ", sum(lista_N)/len(lista_N))
    print("Il massimo tra i numeri inseriti è: ",max(lista_N))
    print("Il minimo tra i numeri inseriti è: ",min(lista_N))
    print()