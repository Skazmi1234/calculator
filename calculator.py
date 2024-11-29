print("welcome! to my simple calculator program ")
print("enter two numbers:")

num1=eval(input("enter first nunmber:"))
num2=eval(input("enter second number:"))

print("choose an operation (+,-,*/):")
operation=input("enter the operation:")
if operation =='+':
  print("Result:",num1+ num2)
elif operation =='-':
  print("Result:",num1-num2)    
elif operation =='*':
  print("Result:",num1*num2)    
elif operation =='/':
  if num2!=0:
   print("Result:",num1/num2)   
  else:
    print("Error:cannot divide by zero..")
else:
  print("Invalid operation..")         