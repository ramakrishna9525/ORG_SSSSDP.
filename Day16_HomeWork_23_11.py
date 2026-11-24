'''
Write  a  program  to  return  list  of  all   prime  numbers  between  2  and  n.
Also  print  number  of  prime  numbers  between  2  and  n.

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers : [2 , 3 , 5 , 7]												
																		   Number  of   prime  numbers : 4
																		  
Hint: Import  prime()  function  defined  in  prog4a  but  do  not  rewrite
'''
from prog4a import prime
def  all_prime_numbers(n):	
	lst = [] #How  to  append  all  the  prime  numbers  to  a  list
	for i in range(2, n+1):
		if prime(i):
			lst.append(i)  #How  to  return  list  of  prime  numbers
	return lst

# End  of  the  function

n = int(input('Enter number of items need in list : ')) # How  to  read  input
x = all_prime_numbers(n) # How  to  call  all_prime_numbers()  function
print(x)# How  to  print  list  of  all  prime  numbers
print(len(x)) # How  to  print  number  of  prime  numbers
