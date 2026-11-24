# Find  outputs
'''How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)'''
import keyword as k
print(k.kwlist)
print(len(k.kwlist))
print(type(k.kwlist))

#  Find  outputs  (Home  work)
'''How  to  import   keyword  module
How  to  print  kwlist
How  to  print  number  of  keywords
How  to  print  type  of kwlist
print(kwlist)'''
import keyword as k
print(k.kwlist)
print(len(k.kwlist))
print(type(k.kwlist))

# How  to  read  float  input ?
x = float(input('Enter  float  number  :  '))
print(type(x)) # <class 'float'>
print(x) # 10.8 <> 25 <> 3+4j <> True





'''
Input     What  does  input()   read      What  does  float(input())  return
---------------------------------------------------------------------------------------
 10.8           string '10.8'              convert string '10.8' to float 10.8 
 25             string '25'                convert string '25' to float 25.0  
 3+4j           string '3+4j'              Error
 True           string 'True'              Error
-----------------------------------------------------------------------------------------
'''

# Identify  the   issue ?
x = bool(input('Enter  Boolean  input  :  '))
print(type(x)) # <class 'bool'>
print(x) 


'''
Input           input()  reads     bool(input())  returns
--------------------------------------------------------------------------
 True             string True           Bool True
 False            string False          Bool False
 <Enter key>      string ''             bool False
 25               string 25             Bool True
 10.8             string 10.8           Bool True
 Hyd              string Hyd            Bool True
 <Space  bar>     string ' '            Bool True
-----------------------------------------------------------------------------------
'''

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) # <class 'complex'>
print(x)


'''
Input       input() reads      complex(input())  returns
------------------------------------------------------------------------
3+4j         string 3+4j               3+4j
4j           string 4j                 4j
j            string j                  Error
25           string 25                 25+0j
10.8         string 10.8               10.8+0j
True         string True               Error
Ten          string Ten                Error
3+j4         string 3+j4               Error
3+4i         string 3+4i               Error
4j+3         string 4j+3               Error <-------
---------------------------------------------------------------------------
'''

# Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25 <------
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd <> None

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # ''
#print(eval('')) # ERROR
print(eval('  " "   ')) # ' '
#print(eval(' ')) # ERROR

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x)) 
print(x)


'''
Input                             input() reads                     eval(input())  returns
--------------------------------------------------------------------------------------
  25                                  '25'                                  25
  10.8                               '10.8'                                10.8  
  3+4j                               '3+4j'                               3 + 4j
  False                              'False'                              False
  None                               'None'                                None
  Hyd                                'Hyd'                                 ERROR 
  'Hyd'                              " 'Hyd' "                             Hyd
  [25 , 10.8 , 'Hyd']           "[25 , 10.8 , 'Hyd']"               [25 , 10.8 , 'Hyd']
---------------------------------------------------------------------------------------------
'''

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a)) # depends on the string we enter
print(a) # prints entered string
b = eval(input('Enter   any  string  : '))
print(len(b)) # if it is non-sequence then error cause it has no indexing and if it sequence it depends on the number
print(b) # entered string is printed

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #  25    10.8    Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25<next-line>10.8<next-line>Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # 25:10.8:Hyd

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25---10.8---Hyd
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd           
print(a , b , c) # 25 10.8 Hyd

# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # ''
print('Sec') # Sec
print() # ''
print('Cyb') # Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a # '25.0'
print(b) # 25.0
print(type(b)) # <class 'str'>
x = 10.8
y = '%i'  %x # '25'
print(y) # 25
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m # '[10,20,15,18]'
print(n) # [10 , 20 , 15 , 18]
print(type(n)) # <class 'str'>

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <4 spaces>10.9
print('%10.3f'  %a) # <2 spaces>10.927
print('%.2f'  %a) # 10.92
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400
print('%g'  %a) # 10.9274

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) # <7 spaces>Hyd
print('%-7s'  %a) # Hyd<7 spaces>
print('%2s'  %a) # <2 spaces>Hyd
print('%s'  %a) # Hyd
print('%s' , a) # %s Hyd
#print('%s'  a) # ERROR % or , is missing
#print('%s' , %a) # ERROR , is not required
print(a) # Hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # '[10,20,30,40]'
print('%s' , a) # %s [10 , 20 , 30 , 40]
print('%s'  a) # ERROR , or % is missing
print('%s' , %a) # ERROR no , is required 
print('%l'  %a) # ERROR %l no method is there
print(a) # [10 , 20 , 30 , 40]

#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd' 
print('%d    %f    %s'  %(a , b , c)) # 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c)) # 25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c)) # 25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c) # %d %g %s 25 10.9274 Hyd
#print('%d    %g      %s'   a , b , c) # ERROR 
#print('%d    %g    %s'  ,  %(a , b , c)) # ERROR
print('%d    %g    %s'    %a%b%c) # 25 10.9274 Hyd <-------
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd

#  Find  outputs  (Home  work)
x = 25
y = F'{x}' # '25'
print(y) # 25
print(type(y)) # <class 'str'
x = 10.8
y = F'{x}' # '10.8'
print(y) # 10.8
print(type(y)) # <class 'str'
x = [10,20,30,40]
y = F'{x}' # '[10,20,30,40]'
print(y) # # [10,20,30,40]
print(type(y)) # <class 'str'

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25  10.8    Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25  b = 10.8  c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25 b=10.8  c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}') # 25   10.8    Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # 25  10.8    Hyd
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a = {a}   b = {b}   c = {c}
#print(F'{x =}  \t   {y =}   \t  {z =}') # ERROR x is not defined 

# Find  outputs
x = 9247
print(x) # 9247
print(F'{x}') # 9247
print(F'{x:7}') #     9247
print(F'{x:07}') # 0009247

# Find  Outputs  (Home  work)
x = 123.9274
print(x) # 123.9247
print(F'{x:8.2f}') #  <3 spaces>123.92
print(F'{x:9.1f}') # <5 spaces>123.9
print(F'{x:10.3f}') # <4 spaces>123.927
print(F'{x:.2f}') # 123.92
print(F'{x:.6f}') # 123.924700
print(F'{x}') # 123.9247

#  Find  outputs  (Home  work)
x = 25
print(F'{x}') # 25
print(F'{{x}}') # {25}
print(F'{{{x}}}') # 
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')