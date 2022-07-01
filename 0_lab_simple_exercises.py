## 1- Print your name and surname
print("Name")
print("Surname")

## 2- Compute the number of days from Jan 1st in the year, given the date 
##    "Dec 13th" (Apr/Jun/Sep/Nov = 30 days, Jan/Mar/May/Jul/Aug/Oct/Dec = 31 days)


## 3- The same as 2., but ask the user for the day of December in the interval 
##    [1,31], and print "ERROR" if the number is not include in the interval 


## 4- Write a program that read two integer inputs (the lenghts of two segments),
##    and computes (and prints) both the area and perimeter of a rectangle (in m2).

a = input("Write an integer "    )
b = input("Write an another integer "    )
a = int(a) ; b = int(b)
area = a*b
perimeter = 2*a + 2*b
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)

## 5- Write a program that asks for a radius (in cm)
##    and prints both the area and the perimeter of a circle.

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