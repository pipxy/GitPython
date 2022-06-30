# Primo codice di prova su python

print("Hello World!")
print("Il programma di questo corso prevede",
      " ...",
      "lo studio del liguaggio python",
      sep=' \n ',
      end='!!!!')

# Prove di definizione variabili

message = 'Questo corso sembra parecchio interessante'
n = 33.3
pi = 3.141592653589793
print(message)
print(message, '--->', type(message))
print('n ->', n, type(n))
print(pi, '--->', type(pi))
print(pi * n)
n = 33.3 + pi
print('n->', n, type(n))

## NB. Caratteristiche di una variabile:
##    - Devono avere un nome significativo
##    - Non possono avere un numero come primo carattere
##    - Meglio utilizzare le minuscole
##    - Meglio utilizzare "_" al posto di " " in variabili con più parole


## Esempio di procedura di definizione errata
## Il codice di seguito non è corretto  e non funziona poichè 
## la variabile t va definita prima della definizione di z.

# z = t
# t = 12
# print(z)


## Esempio di codice che attende un input dalla tastiera

typed_text = input()
print("You typed :", typed_text)
print()
typed_text2 = input("What is your name?  ")
print("You typed : \"", typed_text2, '\"', sep='')

text_num = input("How old are you?  ")
print(type(text_num))
num = int(text_num)
print(type(num))
num = num + 1
print(num)

## ==========================
## Conditionals
## ==========================
## If / if-else
x = input()
x = int(x)        # Trasformo x in numero per poi darlo in pasto al if-else
if x % 2 == 0:
      print(" the first branch was taken.")
      print(' x is even')
else:
      print(x, " is odd.")
      print("ciao")
print("Comando fuori da if-else")

## if-elif-else
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

