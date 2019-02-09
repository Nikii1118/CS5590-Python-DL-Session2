class Employee:
    count=0
    total_sal=0

    def __init__(self,name,family,salary,dept):

       self.full_name=name
       self.family=family
       self.sal=salary
       self.de=dept
       self.__class__.count +=1

    def average_salary(avg_salary):
        sum=0
        for item in avg_salary:
            sum+=item.sal
        return sum/Employee.count


class Fulltime_Employee(Employee):
    def __init__(self,name,family,salary,dept):
        Employee.__init__(self,name,family,salary,dept)





e1=Employee("John cal","cal",10000,"finance")
e2=Employee("allen swift","swift",20000,"finance")
e3=Employee("daniel moon","moon",30000,"finance")

avg_salary=[e1,e2,e3]
avg=Employee.average_salary(avg_salary)
print(avg)
print(Employee.count)
e4=Fulltime_Employee("caroling trrop","stroop",40000,"rsdt")
avg_salary.append(e4)
print(avg)





