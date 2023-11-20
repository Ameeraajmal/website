n1=int(input('enter 1st number:'))
n2=int(input('enter 2nd number:'))
print('1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n')
ch=int(input('enter your choice:'))
if ch==1:
  sum=n1+n2
  print('sum of 2 numbers:',sum)
elif ch==2:
  sum=n1-n2
  print('difference of 2 numbers:',sum)
elif ch==3:
  sum=n1*n2
  print('product of 2 numbers:',sum)
elif ch==4:
  sum=n1/n2
  print('quotient of 2 numbers:',sum)
else:
   print('enter correct choice!!')
