'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i = 2 , 3 , 4 , 5 , 6 , .... 12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i = 2 , 3 , 4 , 5 

4) What  should  be  done  when  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  should  be  done  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  should  be  done  if  there  are  no  divisiors  to  input  number  ? --->  return  True  outside  the  loop
'''
#	return  True  when  'n'  is  prime  number  and  False  otherwise
'''
1) prime(25)  --->  
    How  many  times  is  for  loop  executed ?  --->  

2) prime(11) --->  
    How  many  times  is  for  loop  executed ?  ---> 

3) prime(2) ---> 
    How  many  times  is  for  loop  executed ?  ---> 

4) prime(49) --->  
    How  many  times  is  for  loop  executed ?  --->
'''
def prime(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    try:
        n = int(input('Enter any +ve integer : '))
        if prime(n):
            print('Prime  number')
        else:
            print('Composite  number')
    except :
        print('Invalid Input')
#How  to  read  an  integer  number
#if  input  is  invalid:
#	print('Invalid  input')
#elif  'n'  is  prime  number:
#	print('Prime  number')
#else:
#	print('Composite  number')
