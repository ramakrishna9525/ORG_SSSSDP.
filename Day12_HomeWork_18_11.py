'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  'n'  be  6

What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n = int(input('Enter n terms of fibonacci series : '))
count = 0
a,b = 0, 1
print('Fibonacci Series')
while count < n:
    print(a)
    a, b = b, a+b
    count += 1

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
    print(i, a[i], sep='...')
print('For each loop')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable) -----> Not possible 
'''count = 0
for x in a:
    print(count, x, sep='...')
    count += 1
or use 
for x in a:
    print(a.index(x), x, sep='...')
class enumerate
x = enumerate(a)
print(x)
'''

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(1,len(a)+1):
    print(a[-i])
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice) -----> Not possible
'''for x in reversed(a): or a.reverse()
    print(x)
'''

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for x in range(min(len(a), len(b))):
    e = a[x] + b[x]
    c.append(e)
print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable) ----> Not possible
c = []
count = 0
for i in a:
    f = i + b[count]
    c.append(f)
    count += 1
print('3rd  list : ' , c)
# use zip(a,b) ---> iterators

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
    print(a[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice <--- not possible
for x in a:
    if a[2] == x:
        print(x)
    elif a[3] == x:
        print(x)
    elif a[4] == x:
        print(x)

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1 
print('a :  ' , a) # a :  [11, 21, 15, 18]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #  [10 , 20 , 15 , 18]

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 +  .....

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n
'''
n = int(input('How many terms would you like to add : '))
sum = 0
for i in range(1, n+1):
    a = 1.1 * i
    sum += a
print(f'sum : {sum:.1f}')

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0  + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''
n = 20
sum = 0
for i in range(2, (n*2)+1, 2):
    sum += i
print(f'Sum if first 20 even numbers : {sum}')
sum = 0
for x in range(n+1):
    sum += 2 * x
print(f'Sum if first 20 even numbers : {sum}')

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  .... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
'''
n = 20
sum = 0
for i in range(1, n*2, 2):
    sum += i
print(f'Sum of first 20 odd numbers : {sum}')
add = 0
for x in range(n+1):
    add += 2 * n -1
print(f'Sum of first 20 odd numbers : {sum}')

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''
n = int(input('How many terms would you like to add : '))
sum = 0
for i in range(n+1):
    sum += i
print(f'sum : {sum}')

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2  spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''
n = int(input('Enter how many lines ? : '))
# count = n
for i in range(1, n+1):
    a = '*' * ((2*i)-1)
    b = " " * (n-i) # ' ' * count-1
    c = b + a 
    # count -= 1
    print(f"{c}")

''''
Write  a  program  to  evaluate  expression  like  calculator

Input :  3 + 4 * 5 - 6 / 2 =

What  is  the  output ? --->  14.5

Iteration         a          op        b        result
------------------------------------------------------
     1                 3           +         4           7
     
	 2                7           *         5           35
	 
	 3                35         -          6           29
	 
	 4                29         /          2           14.5
	 
	 5                14.5      =          ----         -----
--------------------------------------------------------
Hint1:  Use  while  loop

Hint2:  Read  whole  expression  as  a  string
'''
n = input('Enter any expression terminated by  = : ')
a = int(n[0])
op = n[1]
i = 2
while op != '=':
	match op:
		case '+':
			a += int(n[i])
		case '-':
			a -= int(n[i])
		case '*':
			a *= int(n[i])
		case '/':
			a /= int(n[i])
	i += 1
	op = n[i]
	i += 1
print('Result :', a)

# 3+4*5-6/2=
n = list(input('Enter any expression terminated by  = : '))
iter = 2
iter2 = 1
sum = int(n[0])
while n[iter2] != '=':
   if n[iter2] == '+':
      sum += int(n[iter])
   elif n[iter2] == '-':
      sum -= int(n[iter])
   elif n[iter2] == '*':
      sum *= int(n[iter])
   elif n[iter2] == '/':
      sum /= int(n[iter])
   iter += 2
   iter2 += 2
print('Result :',sum)

'''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

								n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
        1               3                   2                   n = 21 - 5 = 16
        
		2               1                   4                   n = 16 - 5 = 11
		
		3               2                   3                   n = 11 - 5 = 6
		
		4               4                   1                   n = 6 - 5 = 1
---------------------------------------------------------------
Hint: Use while  loop
'''
n = 21 
while n > 1:
    a = int(input('Enter how matchstiks would you like to pick (1, 2, 3 or 4) ? : '))
    while a > 4 or a < 1:
        a = int(input('Input cannot be > 4 nor < 1, Re-enter : '))
    print(f'Computer picks {5-a} matchsticks')
    n -= 5
print('You have lost the game and computer wins')

n = input('Enter any expression terminated by  = : ')
op = ''
sum = 0
number = ''
iter = 0
while op != '=':
    try:
        int(n[iter])
        number += n[iter]
    except:
        if sum == 0:
            sum = int(number)
        else:
            match op:
                case '+':
                    sum += int(number)
                case '-':
                    sum -= int(number)
                case '*':
                    sum *= int(number)
                case '/':
                    sum /= int(number)
        op = n[iter]
        number = ''
    iter += 1
print(sum)