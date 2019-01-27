
 # 2) ANSWER
print("To count Letters and Digits in a Sentence")
Sentence= input("Enter your sentence")
Digits=0
Letters=0
for i in Sentence:
    if i.isdigit():
        Digits=Digits+1
    elif i.isalpha():
         Letters=Letters+1
    else:
       pass

print("length: " ,Letters)
print("digits: " ,Digits)
# 1) ANSWER
print("To print the strings in reverse")
FirstName= input("Enter your First Name ")
LastName= input("Enter Your Last Name ")
print(FirstName[::-1] + " " + LastName[::-1])
#3 Arithmetic Operators
num1= int(input("Enter the first Number"))
num2=int(input("Enter the second number"))

print("add",num1 + num2)
print("sub",num1 - num2)
print("mul",num1 * num2)
print("div",num1/num2)
print("modulus",num1 % num2)
print("integer",num1//num2)




