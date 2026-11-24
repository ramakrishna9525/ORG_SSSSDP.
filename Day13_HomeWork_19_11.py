'''
Write  a  program  to  print
    A
   A B
  A B C
 A B C D
A B C D E

Input  is  number  of  lines
'''
n = int(input('Enter number of lines : '))
for i in range(1, n+1):
    print(' ' * (n-i), end='')
    for j in range(65, i+65):
        print(chr(j), end=' ')
    print()

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) 
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5 
Sec
Hello
6
7 
Sec
Hello
Outside loop
'''

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # no colon so the error raises
	print('Sec')

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
'''
1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # No colon so the error raises
	print('Sec')