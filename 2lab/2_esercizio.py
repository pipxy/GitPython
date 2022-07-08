## Write the code that prints a pyramid of asterisks of height N;
## for example here one with N=10; note that each line has an odd number of asterisks

#             *
#            ***
#           *****
#          *******
#         *********
#        ***********
#       *************
#      ***************
#     *****************
#    *******************

# Imposto il numero di righe che la mia piramide deve avere, poi aggiungo un asterisco per lato ad ogni riga

N = int(input("Inserisci un numero di righe: "))

for i in range(N):
    print(((N-i)) * " ", (1 + i*2) * "*", sep = "")