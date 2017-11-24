# factorial of a number
"""def fact(z):
    if z==1:
        return z
    else:
        return z*fact(z-1)"""
    
#Multiplication table

"""for s in range(1,6):
    for w in range(1,11):
        print(s,'*',w,'=',s*w)
    print()"""

#Fibonacci series

"""a=0
b=1
count=1
for i in range(1,10):
    c=a+b
    a=b
    b=c
    count+=1
    print(c)"""
#sum of natural numbers

"""num=10
sum=0
while(num>0):
   sum=sum+num
   num-=1
print(sum)"""

#using functions

"""def natural(z):
    if z==1:
        return z
    else:
        return z+natural(z-1)"""

#convert decimal to binary,octal,hexadecimal

"""dec_num=10
print("binary number is :",bin(dec_num))
print("octal number is :",oct(dec_num))
print("hexadecimal number is :",hex(dec_num))"""

#ASCII value of the given character

"""print("ASCII value of S is:",ord('S'))"""

#Add two matrices
"""
x=[[1,2,3],[2,3,4],[3,4,5]]
y=[[1,1,1],[2,2,2],[3,3,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for add_matrix in result:
    print(add_matrix)"""

#Transpose of matrix

"""x=[[1,2],[2,3],[3,4]]
r=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]
for result in r:
    print(result)"""






        
