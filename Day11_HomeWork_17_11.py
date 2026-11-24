'''
Tricky  program
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units	(>= 700)		   	    Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter number of units consumed : '))
match units // 100:
    case 0:
        cost = 3.00 * units
    case 1 :
        cost = 100 * 3.00 + (units - 100) * 3.50 
    case 2 | 3:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:
        cost =  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:
        cost =  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
print('Bill amount : ', cost)

'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  'x'  be   10
What  are  the  outputs  ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

1) What  is  the  formual  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formual  for  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
x = int(input('Enter the value of x : '))
a = 0
b = 1
c = a + b
print('Fibonacci Series')
if x == 0:
    print(a)
else:
    print(a, b, c, sep='\n')
    while c <= x:
        a = b
        b = c 
        c = a + b
        if c <= x:
            print(c)

# Find  outputs
while  True:  
	print('Hello') 
print('Bye') # Infinite Hello

#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye

# Find  outputs  (Home  work)
'''How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop'''
for i in [10 , 20 , 15 , 18]:
    print(i, end = ' ')
for j in 'Hyd':
    print(j, end = ' ')
for x in range(5):
    print(x, end = ' ')

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x , end = '\t') # 10	30	50	
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x , end = '\t') # 20	40	60	
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x , end = '\t') # (10, 20)	(30, 40)	(50, 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , end = '\t') # 10	30	50
print() # prints empty space

# Find outputs  (Home  work)
a = {'AB' : 20 , 'CD' : 40 ,  'EF' : 60}
for  x , y  in   a . items(): 
	print(x , y , sep = '...')  # ('AB', 20)...('CD', 40)...('EF', 60)
print()	# prints empty 
for  x ,  y  in   a:    
	print(x , y , sep = '...') 
print()	# prints empty
for  x , y  in  {'AB' : 20 ,  'CDE' : 40 ,  'FGHI' : 60}: 
	print(x , y , sep = '...') # 
for  x , *y  in  {'AB' : 20 ,  'CDE' : 40 ,  'FGHI' : 60}:  
	print(x , y , sep = '...') # 

# Identify  error  (Home  work)
for  x  in   123: # 123 is non-sequence but required a sequence nummber
        print(x) 

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # nothing
for  x   in  []: # nothing
        print(x)
for  x   in   {}: # nothing
        print(x)
for  x   in   set(): # nothing
        print(x)
for  x   in   '': # nothing
        print(x)
for  x  in  range(10 , 10): # nothing
	print(x)
for  x  in   range(): # range needs alteast one arg
	print(x)
for  x  in   (25): # ERROR cause non-sequence is not valid
	print(x)

'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20
'''
a = int(input('Enter how many first even number you want : '))
print(f'First {a} even numbers')
for i in range(1,a+1):
    print(f'{2*i}', end = ' ')

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  ---> 1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20
'''
a = int(input('Enter how many first even number you want : '))
print(f'First {a} odd numbers')
for i in range(1,a+1):
    print(f'{(2*i)-1}', end = ' ')

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n
'''
a = int(input('Enter how many first even number you want : '))
print(f'First {a} natural numbers')
for i in range(1,a+1):
    print(f'{i}', end = ' ') 

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1
'''
a = int(input('Enter how many first even number you want : '))
print(f'Numbers from {a} down to 1 in steps of -1')
for i in range(a, 0,-1):
    print(f'{i}', end = ' ')

'''
Write  a  program  to  print  upper  and  lower  case  alphabets

1) What  is  chr(65)  ?  --->  A

2) What  is  chr(90)  ?  --->  Z
 
3) What  is  chr(97)  ?  --->  a

4) What  is  chr(122)  ?  --->  z
'''
for i in range(65, 91):
    print(chr(i), end = ' ')
print()
for j in range(97, 123):
    print(chr(j), end = ' ')

# Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye') 
''' 
1 1 
1 2 
1 3 
1 4 
Hello
2 1 
2 2 
2 3 
2 4 
Hello
3 1 
3 2 
3 3 
3 4 
Hello
Bye
'''

# Find  outputs
for i in range(3):
	for i in range(5):
		pass
	print(i) # 4 <> 4 <> 4