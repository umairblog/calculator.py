def Addition(num1,num2):
    return num1+num2
def Subtraction(num1,num2):
    return num1-num2
def Multiplication(num1,num2):
    return num1*num2
def Division(num1,num2):
    return num1/num2

print("welcome to the Calculator")
print("=========================================================")
print("please select operations -\n"
      "1-Addition \n"
      "2-Subtraction \n"
      "3-Multiplication \n"
      "4-Division \n")

Select= int(input("select operations from 1,2,3,4:"))

num1= int(input("select first number: "))
num2= int(input("select second number: "))

if Select ==1:
    print(num1,"+",num2,"=",Addition(num1,num2))
elif Select ==2:
     print(num1,"-",num2,"=",Subtraction(num1,num2))
elif Select ==3:
     print(num1,"*",num2,"=",Multiplication(num1,num2))
elif Select ==4:
     print(num1,"/",num2,"=",Division(num1,num2))
else :
    print("Invalid Input")




