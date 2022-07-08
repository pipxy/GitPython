## Given a function on 2 variables (x,y) 
##            x^3 − y^2 + y -3*x
## find the pair of integer values that maximize the function 
## (suppose N and M the maximum range for x and y respectively).

def equazione(x,y):
    return (x**3)-(y**2)+y-(3*x)

# start here

N = int(input("Inserisci un numero massimo che x può assumere "))
M = int(input("Inserisci un numero massimo che y può assumere "))

max = equazione(0,0)

for i in range(N):
    for j in range(M):
        result = equazione(i,j);
        if result > max:
            max = result
            x_max = i ; y_max = j

print("Valore massimo assunto dalla funzione", max)
print("Il valore di x che massimizza la funzione è ", x_max); print("Il valore di y che massimizza la funzione è ", y_max)