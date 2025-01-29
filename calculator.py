num1=float(input("Your first number: "))
num2=float(input("Your second number: "))
inq=input("What do you wanna do with them?: ").lower()
if inq=="multiply":
    print("",num1*num2)
elif inq=="divide":
    print("", num1/num2)
elif inq=="sum":
    print("",num1+num2)
elif inq=="subtraction":
    print("",num1-num2)