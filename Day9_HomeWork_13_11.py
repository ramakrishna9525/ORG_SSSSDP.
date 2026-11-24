'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  ---> 2 * (length + breadth)
'''
try:
    l = float(input("Enter Length of Rectangle : "))
    b = float(input("Enter breadth of Rectangle : "))
    area = l * b
    perimeter = 2 * (l+b)
    print(f'Area : {area:.2f}')
    print(f'Perimeter : {perimeter:.2f}')
except:
    print('The input should be Integer (or) Float')

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
try:
    import math as m
    r = float(input("Enter radius : "))
    v = 4/3 * m.pi * m.pow(r,3)
    print(f'Volume : {v:.2f}')
except:
    print('The input should be Integer (or) Float')


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
try:
    p = float(input('Enter principle : '))
    t = float(input('Enter time in years : '))
    r = float(input('Enter rate of interest : '))
    si = (p*t*r)/100
    ci = p * (1 + r / 100) ** t -p
    print(f'Simple Interest : {si:.2f}')
    print(f'Compound Interest : {ci:.2f}')
except:
    print('Input should be in form of integer (or) float')

'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j

What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                          = (15 - 18j + 20j + 24)  / (25 + 36)											   
																          =  39 / 61 +  2j/61
'''
try:
    x = complex(input('Enter first complex number : '))
    y = complex(input('Enter second complex number : '))
    sum = (x) + (y)
    diff = (x) - (y)
    prod = (x) * (y)
    div = (x) / (y)
    print(f'Sum : {sum}')
    print(f'Difference : {diff}')
    print(f'Product : {prod}')
    print(f'Division : {div}')
except: 
    print(f'Enter the inputs in form of integer or float')

'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  ---> 17 
What  is  the  difference ?  ---> 3
What  is  the  product ?  --->  70
What  is  the  quotient ?  ---> 1.42
What  is  the  remainder ?  ---> 3
What  is  the  largest  number ?  ---> 10
What  is  the  smallest  number ?  ---> 7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power?  --->  10 ^ 7 = 10000000
What  is  the  gcd  of  2  numbers ?  --->  1
What  is  the  factorial   of  1st  input ?  ---> 10!
'''
import math as m 
try:
    x = int(input('Enter 1st integer number : '))
    y = int(input('Enter 2nd integer number : '))
    print(f'{x} + {y} = {x + y}')
    print(f'{x} - {y} = {x - y}')
    print(f'{x} * {y} = {x * y}')
    print(f'{x} / {y} = {x / y}')
    print(f'{x} % {y} = {x % y}')
    print(f'max{x,y} = {max(x,y)}')
    print(f'min{x,y} = {min(x,y)}')
    print(f'{x} ^ {y} = {x ** y}')
    print(f'sqrt({x}) = {m.sqrt(x)}')
    print(f'gcd{x,y} = {m.gcd(x,y)}')
    print(f'fact({x}) = {m.factorial(x)}')
except ValueError:
    print('Enter inputs in form of intergers')

'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
x = input('Enter 1st input : ')
y = input('Enter 2nd input : ')
print(f'Before swap : {x=}  {y=}')
temp = x
x = y 
y = temp
print(f'After swap : {x=}  {y=}')

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  reference

Hint: One  addition  and  two  subtractions

x = 25
y = 10
'''
x = int(input('Enter 1st input : '))
y = int(input('Enter 2nd input : '))
print(f'Before swap : {x=}  {y=}')
x = x + y
y = x - y 
x = x - y
print(f'After swap : {x=}  {y=}')

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  reference

Hint: One  multiplication  and  two  divisions

x = 25
y =  10
'''
x = int(input('Enter 1st input : '))
y = int(input('Enter 2nd input : '))
print(f'Before swap : {x=}  {y=}')
x = x * y
y = x // y 
x = x // y
print(f'After swap : {x=}  {y=}')

'''
Tricky  program
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  reference

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = input('Enter 1st input : ')
y = input('Enter 2nd input : ')
print(f'Before swap : {x=}  {y=}')
x, y = y, x
print(f'After swap : {x=}  {y=}')

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   ---> 20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   ---> 'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
try:
    x = eval(input("Enter 1st input : "))
    y = eval(input('Enter 2nd input : '))
    z = eval(input('Enter 3rd input : '))
    max = x if (x>y) and (x>z) else y if (y>x) and (y>z) else z
    print(f'Larger Input : {max}')
except TypeError:
    print('Input should not be a complex number')

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  ---> >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  nested  ternary  operator
'''
try:
    x = eval(input('Enter 1st input : '))
    y = eval(input('Enter 2nd input : '))
    max = '>' if x > y else '<' if y > x else '='
    print(f'Result : {max}')
except TypeError:
    print('Input should not be a complex number')

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  ---> -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
try:
    x = float(input('Enter any number : '))
    result = 1 if x>0 else -1 if x<0 else 0
    print(f'Result : {result}')
except ValueError:
    print('Enter input in form of integer or float')

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  ---> Divisible  by  2


2) What  is  an  odd  number  ?  ---> Not  divisible  by  2

3) Use  ternary  operator
'''
try:
    x = int(input('Enter any +ve integer : '))
    result = 'even' if x%2 == 0 else 'odd'
    print(f'{result} number')
except ValueError:
    print('Enter input in form of integer')
    
"""
# Identify  error
#else:
#		print('else  suite')  # ERROR cause else should contain only after if block
print('Outside') # Outside

# Identify  error
'''if  9 > 5 # No semi-colon so error raises 
	print('Hello')'''
print('Bye') # Bye

# Identify  error
'''if  9 > 12:
	print('Hyd')
else # No semi-colon so raises error'''
	print('Sec')

# Identify  error
if  (10,20,15):
print('Hyd') # Indentation Error 
else:
print('Sec')

# Identify  error
if  ():
			print('Hyd')
	else: # else should have same column as if block
					print('Sec')
print('Bye')

# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
} # No need of braces here
print('Bye')


# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: # Indentation
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: # Indentation
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
"""

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
    x = int(input('Enter any +ve number : '))
    if x % 2 == 0:
        print(f'Even number')
    else:
        print(f'Odd number')
except ValueError:
    print('Enter input in form of integer or float')

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
'''
One
Two
Three
Bye
'''

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
'''
Hyd
Sec
Cyb
Bye
'''

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    x = int(input('Enter month number (1-12):'))
    if x == 1:
        print('January')
    elif x == 2:
        print('Febraury')
    elif x == 3:
        print('March')
    elif x == 4:
        print('April')
    elif x == 5:
        print('May')
    elif x == 6:
        print('June')
    elif x == 7:
        print('July')
    elif x == 8:
        print('August')
    elif x == 9:
        print('September')
        print('October')
    elif x == 10:
        print('September')
        print('October')
    elif x == 11:
        print('November')
    elif x == 12:
        print('December')
    elif x > 12 :
        print('Input should be between 1 and 12')
except ValueError:
    print('Input should be an integer')


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
try:
    x = int(input('Enter any digit (0-9):'))
    if x == 0:
        print('Zero')
    if x ==1:
        print('One')
    if x == 2:
        print('Two')
    if x == 3:
        print('Three')
    if x == 4:
        print('Four')
    if x == 5:
        print('Five')
    if x == 6:
        print('Six')
    if x == 7:
        print('Seven')
    if x == 8:
        print('Eight')
    if x == 9:
        print('Nine')
    else: 
        print('Not a digit')
except ValueError:
    print('Input should be an integer')

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? ---> Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  ---> Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
x = int(input('Enter 4-digit year : '))
if x % 4 == 0:
    print('Leap year')
elif x % 400 == 0:
    print('Leap year')
else:
    print('Not a leap year')

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
try:
    x = eval(input('Enter 1st input : '))
    y = eval(input('Enter 2nd input : '))
    z = eval(input('Enter 3rd input : '))
    if x>y and x>z:
        print(f'Largest number : {x}')
    elif y>x and y>z:
        print(f'Largest number : {y}')
    elif z>x and z>y:
        print(f'Largest number : {z}')
except NameError:
    print('String should be in Quotes("")')

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? ---> 1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  ---> (temp - 32) / 1.8
'''
try:
    x = int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
    if x == 1:
        temp = float(input('Enter celsius temparature : '))
        result = 1.8 * temp + 32
        print(f'Fahrenheit Equivalent : {result:.2f}')
    elif x == 2:
        temp = float(input('Enter fahrenheit temparature : '))
        result = (temp - 32) / 1.8
        print(f'Celsius equivalent : {result:.2f}')
    elif x > 2:
        print('Enter integer number 1 or 2')
except ValueError:
    print('Enter integer number 1 or 2')

'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  ---> 'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  ---> 'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  ---> 'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif  .... else
'''
try:
    a = eval(input('Enter a tuple of (x co-ordinate, y co-ordinate) : '))
    if type(a) == tuple:
        x, y = a
        if x > 0 and y > 0:
            print('1st quadrant')
        elif x < 0 and y > 0:
            print('2nd quadrant')
        elif x < 0 and y < 0:
            print('3rd quadrant')
        elif x > 0 and y < 0:
            print('4th quadrant')
        elif (x>0 or x<0) and y == 0:
            print('On x-axis')
        elif (y<0 or y>0) and x == 0:
            print('On y-axis')
        elif x == 0 and y == 0:
            print('On Origin')
        else:
            print('Enter correct values')
    else:
        print('Enter values in a tuple')
except NameError:
    print('Enter values in a tuple')
except TypeError:
    print('Enter numbers only')