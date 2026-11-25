# # '''
# # Write   a  function  to  test  a  number  is  prime  (or)  not.
# # 1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

# # 2) Let  input  be  25
# #     What  is  the  range  of  divisors ? --->  i = 2 , 3 , 4 , 5 , 6 , .... 12

# # 3) Let  input   be  11
# #     What  is   the  range  of  divisors ? ---> i = 2 , 3 , 4 , 5 

# # 4) What  should  be  done  when  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

# # 5) What  should  be  done  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

# # 6) What  should  be  done  if  there  are  no  divisiors  to  input  number  ? --->  return  True  outside  the  loop
# # '''
# def   prime(n):
# 	return  True  when  'n'  is  prime  number  and  False  otherwise
# '''
# 1) prime(25)  --->  
#     How  many  times  is  for  loop  executed ?  --->  #9 times

# 2) prime(11) --->  
#     How  many  times  is  for  loop  executed ?  ---> #4 times

# 3) prime(2) ---> 
#     How  many  times  is  for  loop  executed ?  ---> one time

# 4) prime(49) --->  
#     How  many  times  is  for  loop  executed ?  --->#16time
# '''
# # How  to  read  an  integer  number
# if  input  is  invalid:
# 	print('Invalid  input')
# elif  'n'  is  prime  number:
# 	print('Prime  number')
# else:
# 	print('Composite  number')


def prime(n):
	if n<=1:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
		

n=int(input("Enter Any input"))
if n<1:
	print("Invalid Input")
elif prime(n):
	print("Prime Number")
else:
	print("Composite Number")



# def   f1():
# 	write  logic
# Read  inputs
# Call  the  function
# print  the  results



# Find  outputs  (Home  work)
# def   disp(empno , ename , sal):
#         print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# # End  of  the  function
# disp(25 , 'Rama  Rao' , 10000.0)#Emp Number : 25 Emp Name : Rama Rao Salary :10000.0
# disp('Sita' , 20000.0 , 35)#Emp Numbe : Sita  Emp Name:20000  Salary:35



# # # Modify  following  program  such  that  every  function  should  be  executed
# def  f1():
# 	print('No-argument  function')
# def  f1(x):
# 	print('Single  argument  function  : ' , x)
# def  f1(x , y):
# 	print('Two  argument  function : ' , x , y)
# def  f1(x , y , z):
# 	print('Three  argument  function : ' , x , y , z)
# f1(10 , 20 , 30)#Three  argument  function :10 , 20 , 30



# #     # Find  outputs (Home  work)
# def  f1():
# 	print('No-argument  function')
# def  f1(x):
# 	print('Single  argument  function  : ' , x)
# def  f1(x , y):
# 	print('Two  argument  function : ' , x , y)
# def  f1(x , y , z):
# 	print('Three  argument  function : ' , x , y , z)
# f1(10 , 20 , 30)# Three argument function:10 20 30
# # f1(40 , 50)#Error
# # f1(60)#Error
# # f1()#Error



# # #  Find  outputs (Home  work)
# def   add(a , b):
#         return  a + b
# #End  of  the  function
# print(add(10 , 20))  #  30
# print(add('Hyder' , 'abad'))#Hyderabad
# print(add(10.8 , 20.6))#31.4
# print(add(True , False))#True
# print(add(3 + 4j , 5 + 6j))#8+10j
# print(add(25 , 10.8))#35.8
# print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#25,10.8,Hyd,True,None,3+4j,Sec
# print(add(10 , '20'))#Error bcoz nonsequence not accept the sequence


# Find  outputs
# def  f1():
# 		print('f1  Function')
# 		f2()
# #f2()#initially it does not but later #f2 function		
# def  f2():
# 		print('f2  function')
# f1()#f1 function


# # # Find  outputs
# # How  to  import  function  f1()  from  prog7a 
# # def   f1():
# # 	print('Function  of  prog7c')
# # How  to  call  function  f1()   of  prog7a
# # How  to  call  function  f1()   of  prog7c (i.e. current  program)
# # prog7a . f1()


# # # Find  outputs
# # def   f1():
# # 	print('Function  of  prog7b')
# # How  to  call  function  f1()   of  prog7a #from prog7a import
# # How  to  call  function  f1()   of  prog7b (i.e. current  program)


# # # This  is  not  a  home  work
# # # Can  function  of  a  program  be  called  from  a  different  program ?
# # def  f1():
# # 	print('Function  of  prog7a')



# # '''
# # py  prog7a.py
# # What  are  the  outputs ?  ---> No  outputs  becoz  function  f1()  is  not  called
# # '''


#  Find  outputs
# def    f1():
#         print('Hyd')
#         print('Sec')
#         print('Cyb')
# # End  of  the  function
# print('Begin')#Begin
# print(type(f1))#class function
# print(id(f1))#Address of the function
# print('End')#End



# Find  outputs  (Home  work)
# print('Hello')#Hello
# def  f1():
#         print('f1  function')#None
# # End  of  the  function
# print('Hi')#Hi
# print(f1())#fl function
# print(f1)#address and type
# print('Bye')#Bye


# # Find  outputs
# def    f1():
# 	return  10
# 	return  20
# 	return  30
# # End  of  the  function
# print('Begin')#Begin
# x = f1()  
# print(x)# 10
# print('End')#End
# return   100


# # Find  outputs  (Home  work)
# def  f1():
# 	return   10 , 20 , 30
# # End  of  the  function
# x = f1() #10 ,20,30
# print(x)
# print(type(x))#class tuple
# a , b , c =  f1()   
# print(a)#10
# print(b)#20
# print(c)#30
# print('for  loop')#for loop
# for  x   in   f1():
# 	print(x)#10 <next line>20<next line>30


    # Find outputs  (Home  work)
# def   f1():
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# # End  of  the  function
# print('Begin')#Begin 
# x = f1()  #
# print(x) #Hyd   <next line> #Sec <next line> Cyb
# print(type(x))#class function  
# print('End')#'End'



# return  statement  demo  program
# def  f1():
# 	print('f1  function')
# 	return  25  
# 	print('Hello') #None
# # End  of  the  function
# print('Begin')#Begin
# x =  f1() #25
# print(x) #f1 function
# print('End')#End


# '''
# Modify  following   program  with  walrus  operator
# Hint:  Combine  lines  6  and   8  to a  single  line  with   walrus  operator
# '''
# sum =  ctr = 0
# while  x:=eval(input('Enter input  (ctrl + z  to  stop)  :  ')):
# 	try:
# 		# x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))  
# 		sum += x 
# 		ctr +=1  
# 	except  EOFError:
# 		try:
# 			print('Average : ' , sum / ctr)  
# 			exit()
# 		except  ZeroDivisionError:
# 			print('Enter  at  least  one  input')
# 	except  NameError , TypeError:
# 		print('Input  cannot  be  string')



    