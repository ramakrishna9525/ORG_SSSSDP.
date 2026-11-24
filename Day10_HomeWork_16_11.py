# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
    a = int(input('Enter any number between (1 - 12) : '))
    if a < 13:
        lst = ['January', 'Febraury', 'March', 'April','May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December']
        print(lst[a-1])
    else:
        print('Enter number between 1 and 12')
except:
    print('Enter a integer number')

'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max =  20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  a

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  and  elif  in  the  program
'''
try:
    a = float(input("Enter first input : "))
    b = float(input("Enter second input : "))
    c = float(input("Enter third input : "))
    max = a 
    min = b
    if max < a :
        max = a 
    if max < b:
        max = b
    if max < c:
        max = c
    print(f'Largest input : {max:.1f}')
    if min > a:
        min = a
    if min > b:
        min = b
    if min > c:
        min = c
    print(f'Smallest input : {min:.1f}')
    mid = (a+b+c) - (max+min)
    print('Middle input', '%.1f' %mid)
except ValueError:
    print('Input should be in form of float (or) integer number')


'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  ---> (a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  ---> a + b + c

4) What  is  the  qualification  of  triangle  ?  ---> Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''
import math as m
try:
    a = float(input('Enter 1st side : '))
    b = float(input('Enter 2nd side : '))
    c = float(input('Enter 1st side : '))
    if a + b > c and b + c > a and c + a > a:
        if a == b == c :
            area = m.sqrt(3) / 4 * a ** 2
            print(f'Equilateral triangle\nPerimeter : {area:.2f}')
        elif a == b or b == c or c == a:
            perimeter = a + b + c
            print(f'Isoceles triangle\nPerimeter : {perimeter:.2f}')
        else:
            s = (a + b + c) / 2
            perimeter = a + b + c 
            area = m.sqrt(s * (s-a) * (s-b) * (s-c))
            print(f'Scalene triangle\nArea : {area:.2f}')
            print(f'Perimeter : {perimeter:.2f}')
    else :
        print('Not a triangle')
except ValueError:
    print('Input should be Integer or float number')

'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  ---> b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  ---> Real  and  distinct
     What  is  the  formula  for  root1  ?  ---> (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  ---> (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  ---> Real  and  same
     What  is  the  formula  for  root  ?  ---> -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  ---> Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  ---> -b / 2a
	 What  is  the  formula  for  imag  part ?  ---> sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j
'''
import math
try:
     a = float(input('Enter value of a : '))
     if a != 0:
          b = float(input('Enter value of b : '))
          c = float(input('Enter value of c : '))
          discriminant = b ** 2 - 4 * a * c
          if discriminant > 0 :
               print('Roots are real and distinct')
               root1 = (-b + m.sqrt(discriminant)) / (2 * a)
               root2 = (-b - m.sqrt(discriminant)) / (2 * a) 
               print(f'Root 1 : {root1:.2f}')
               print(f'Root 2 : {root2:.2f}') 
          elif discriminant == 0:
               print('Roots are Real and equal')
               root = -b / (2 * a)
               print(f'Root1 : {root:.2f}')
               print(f'Root2 : {root:.2f}')  
          else:
               print('Roots are imaginary (or) complex')
               real = -b / (2 * a)
               imag = m.sqrt(-discriminant) / (2 * a)
               result = complex(real, imag)
               result1 = complex(real, -imag)
               print(f'Root 1 : {result}')
               print(f'Root 2 : {result1}')
     else :
          print('Value of a can not be 0')
except ValueError:
     print('Input should be an integer (or) float')

'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  ---> sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math as m
try:
    a = eval(input('Enter a tuple of (x co-ordinate , y co-ordinate) : '))
    if type(a) == tuple:
        x, y = a
        r = float(input('Enter radius of circle : '))
        dist = m.sqrt(x ** 2 + y ** 2)
        if dist > r:
            print('Point is outside the circle')
        elif dist < r:
            print('Point is inside the circle')
        else:
            print('Point is on the circle')
    else:
        print('Enter values in form of tuple')
except TypeError:
    print('Values should not be complex or strings')
except NameError:
    print('Values must and should be in tuple')

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  # Bye

"""# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') #ERROR cause anonymous object should present at end """

"""# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # ERROR only one anonymous should be present"""

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # Hyd <> Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') # Book <> Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd <> Sec <> Cyb <> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One <> Two <> Three <> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India <> China <> Usa <> Bye 
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd <> Sec <> Cyb <> Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One <> Two <> Three <> Bye
6) What  are  the  outputs  if  input  is  7  ?  --->  Hyd <> Sec <> Cyb <> Bye
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')		
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')		 
		print('Three')
	case  _:
		print('India')
		print('China')		
		print('Usa')
# End  of  match
print('Bye') 

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Not a point <----
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> Not a point <------
8) What  is  the  output  when  input  is  ()  ?  ---> # Not a point 
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> # Not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> # Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> # Not a point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')

n = float(input('Number of inputs : '))
lst = list(map(float, input('Enter the numbers seperated by space :').split()))
if n == len(lst):
    lst.sort()
    min = lst[0]
    max = lst[-1]
    mid = lst[len(lst)//2]
    print(f'Largest number : {max:.0f}')
    print(f'Middle number : {mid:.0f}')
    print(f'Smallest number : {min:.0f}')
else:
    print('Enter same number of elements as desired nummber of inputs')