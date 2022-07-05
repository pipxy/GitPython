## 1- Print your name and surname
print("====== ESERCIZIO 1 =====")
print("Name")
print("Surname")

## 2- Compute the number of days from Jan 1st in the year, given the date 
##    "Dec 13th" (Apr/Jun/Sep/Nov = 30 days, Jan/Mar/May/Jul/Aug/Oct/Dec = 31 days)
print("====== ESERCIZIO 2 =====")

days30 = 4 * 30
days31 = 6 * 31
daysDec = 13
daysFeb = 28
print("days from Jan 1st to Dec 13th:", days30 + days31 + daysDec + daysFeb)


## 3- The same as 2., but ask the user for the day of December in the interval 
##    [1,31], and print "ERROR" if the number is not include in the interval 
print("====== ESERCIZIO 3 =====")

daysDec = int(input("Day of Dec: "))
if daysDec < 1 or daysDec > 31:
  print("ERROR")
else:
  days30 = 4 * 30
  days31 = 6 * 31
  daysFeb = 28
  print("days from Jan 1st to Dec 13th:", days30 + days31 + daysDec + daysFeb)


## 4- Write a program that read two integer inputs (the lenghts of two segments),
##    and computes (and prints) both the area and perimeter of a rectangle (in m2).
print("====== ESERCIZIO 4 =====")
a = input("Write an integer "    )
b = input("Write an another integer "    )
a = int(a) ; b = int(b)
area = a*b
perimeter = 2*a + 2*b
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)

## 5- Write a program that asks for a radius (in cm)
##    and prints both the area and the perimeter of a circle.
print("====== ESERCIZIO 5 =====")

import math

radius = input("Write the radius for a circle (in cm)  ")
radius = int(radius)
area_cir = math.pi * radius**2
per_cir = 2 * radius * math.pi
print("The area of the circle is: ", area_cir)
print("The perimeter of the circle is: ", per_cir)

## 6- Suppose that the cover price of a book is EUR 15.90,
##    but a bookstore gets a x% discount. Shipping costs EUR 3 
##    for the first copy and 75 cents for each additional copy. 
##    Ask the user for typing the discount percent and the number
##    of copies to ship. The program has to return on the screen
##    the total cost. Print also the cost with a VAT of 23%.a
print("====== ESERCIZIO 6 =====")

book_in_price = 15.90
first_sped = 3
altre_sped = 0.75
VAT = 0.23
print("The price of the book is ", book_in_price)
discount = input("Write a discount percentage  ") 
discount = int(discount)
copies = input("How many copies do you want?   ")
copies = int(copies)
book_fin_price = book_in_price - book_in_price * (discount/100)
final_price = book_fin_price*copies + first_sped + altre_sped*(copies - 1)
print("The total cost (no VAT) is: ", final_price)
print("The total cost is ", final_price + (final_price*VAT))

## 7- Given 3 integer numbers, whose meanings are current time in hour,
##    minutes, and seconds, compute how many seconds have passed from 
##    the beginning of the day. Ask the user for the three numbers and
##    print the results on the screen. 

print("====== ESERCIZIO 7 =====")

orario = input("Inserisci ore, minuti e secondi separati da uno spazio (ex. 4 32 56 sono quattro ore, 32 minuti e 56 secondi) ")
print("Hai inserito ", orario)
ora = orario.split(" ")
ore = int(ora[0]) ; minuti = int(ora[1]) ; secondi = int(ora[2])
second_passed = secondi + minuti*60 + ore*60*60
print("Il numero di secondi trascorsi è ", second_passed)

## 8- The same as exercise 7, but computes the total number of minutes
##    from the beginning of the days as a real (float) number
##    (ex: 2:23:3 corresponds to 143.05 minutes).

print("====== ESERCIZIO 8 =====")

orario = input("Inserisci ore, minuti e secondi separati da uno spazio (ex. 4 32 56 sono quattro ore, 32 minuti e 56 secondi) ")
print("Hai inserito ", orario)
ora = orario.split(" ")
ore = int(ora[0]) ; minuti = int(ora[1]) ; secondi = int(ora[2])
minutes_passed = float(ore*60 + minuti + (secondi//60) + (secondi % 60))
minutes_passed_dec = float(ore*60 + minuti + (secondi/100))
print("Sono trascorsi ", minutes_passed , " minuti")
print("oppure")
print("Sono trascorsi ", minutes_passed_dec, "minuti (calcolati in base 10 e con 2 cifre decimali")

##  9- Ask the user for the three coefficients a, b, and c of a quadratic equation, and find its solutions x.
##     Hint: to use the square root, we need the extra module software math.
import math
a = input("Inserisci un numero a: ")
b = input("Inserisci un numero b: ")
c = input("Inserisci un numero c: ")
a = float(a) ; b = float(b) ; c = float(c)

delta = b**2 - 4*a*c
root = math.sqrt(delta)
x1 = (-b + root)/2*a
x2 = (-b - root)/2*a
print(x1, x2)


## 10- Given 3 integer numbers, check if they can be the lengths of the sides of a right triangle.
##     (Hint: Apply the Pythagorean theorem.)

# The sides of a right triangle must have lengths that are coherent with their angles.
# A right triangle has a 90degrees angle, so the other two angles must be a1+a2 = 90°
# This leads to the Pitagora theorem: it states that the area of the square with side equal to the side
# in front of the right angle must be equal to the sum of the areas of the two squares with sides equal to
# the other sides of the triangle.

# I want the script to:
# - take side a, b and c length
# - compute the areas of the 3 triangles
# - spot the ipotenusa, which is the longest side
# - compare the area of the ipotenusa-square  with the sum of the other two side-square
# - if those are equal, then TRUE. Else FALSE

import numpy

print("You will be asked to provide the length of 3 sides of a triangle ...")
a = int(input("Length of side 1 > "))
b = int(input("Length of side 2 > "))
c = int(input("Length of side 3 > "))

print(a,b,c)

# If a side is longer than the others, than it is the Ipotenusa

ipo = max(a,b,c)
lati = numpy.array([a,b,c])
lati.sort()
cateto1 = lati[1]
cateto2 = lati[2]

if ipo**2 == cateto1**2 + cateto2**2:
  print("These integers could be sides of a right triangle")
else:
  print("These integers cannot be sides of a right triangle")
print("Esercizio finito")