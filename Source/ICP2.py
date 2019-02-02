#avg of the number
N=int(input("Enter the number of plants"))
sum = 0
x=input()
num=x.split()
for i in num:
   sum = sum + int(i)
print(round(sum/N,3))

#stack and queues
x=int(input("Enter the input 0:stack,1:queue"))

if x==0:
    list = []
    print("Enter an element in the stack")
    list.insert(0,input())
    print("Enter 1 to push in stack")
    print("Enter 2 to pop in stack")
    print("Enter 3 to print the stack")
    num = int(input())
    while list!=[]:
         if num==1:
          list.append(input())
         elif num==2:
          list.pop()
         elif num==3:
          print(list)
         print("Enter 1 to push in stack")
         print("Enter 2 to pop in stack")
         print("Enter 3 to print the stack")
         num = int(input())
    print("list is empty")
elif x==1:
    queue=[]
    queue.append(input())
    queue.append(input())
    print(queue)
    queue.pop()
    print(queue)
else:
    print("invalid number")



#uppercase_to_lowercase and viceversa
str=input()
print(str.swapcase())






