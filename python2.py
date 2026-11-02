
# SECTION A

# b. Guido van Rossum
# c. #
# c. student_name
# b. float
# b. 3
# c. if-elif-else
# b. for
# c. def
# b. return
# b. To document a function/class/module

# SECTION B


##Que 11 : python is a high level interpreted object oriented,
##         globally used programming language with easy to read syntax
##         it is used in Web developement, Machine learning, DataScience,
##         Artificial Intelligence, Automation etc..
##
##         Features of Python : 1. Cross Platforms
##                              2. Huge Library support
##                              3. Object oriented
##                              4. Easy to understand


##Que 12 : A variable is like a container
##         in python which stores values inside it.
##
##         variable name cannot start with numerical value
##         or special character..
##
##         variable name can be alhabetic or use '_' for joining
##         two words
##
##         For ex: stu_name, name, stu1


##Que 13 : There are four built in datatype in python are
##         integer, string, float and boolean...
##
##         a)Integer containes whole numbers, it is basically
##           stores numberical value
##
##           ex : age = 66
##
##         b)String contains alphabetic values uses "", '',
##           single or duble quation to represent
##
##           ex : name = "vaishnavi" / name = 'vaishnavi'
##
##           c)Float is used to store the decimal values with points
##
##             ex : price = 20000.00
##
##           d)Boolean Represents the values like True or False based
##             on condition
##
##             ex : 11 > 12 returns False
##                  12 > 9 returns True

##Que 14 : the difference between / and // are:
##
##            / is used to give decimal value after division
##            while // is used to give value in whole number or round off
##
##            For ex : 10 / 3 ==> 3.33...
##                     10 // 3 ==> 3


##Que 15:  Fuctions are the reuable block of code...
##           and define by 'def' keyword..
##
##           there are 5 differnt type of fuctions can be used in python
##
##           1. Parameterized functions
##           2. Non Parameterized functions
##           3. function with default parameter
##           4. function with return type
##           5. Nested function
##           6. lambda function
##
##           Ex  : def fun_name():
##                       return ___


# SECTION 3
##Ques : 16

##class Student:
##    def __init__(self, name, marks):
##        self.name = name
##        self.marks = marks
##
##    def display(self):
##        print(f"Student Name : {self.name}\nMarks: {self.marks}")
##
##obj1 = Student("Rahul", 85)
##obj1.display()

##Ques : 17
##
##class Calculation:
##
##    def __init__(self, num1, num2):
##        self.num1 = num1
##        self.num2 = num2
##
##    def add(self):
##        print("Addition: ", num1+num2)
##
##    def sub(self):
##        print("Substraction: ", num1-num2)
##
##    def mul(self):
##        print("Multiplication: ", num1*num2)
##
##    def div(self):
##        print("Division: ", num1/num2)
##
##    def mod(self):
##        print("Modulus: ", num1%num2)
##
##obj1 = Calculation(5,2)
##obj1.add()
##obj1.sub()
##obj1.mul()
##obj1.div()
##obj1.mod()

##Ques : 18

##n = int(input("Enter number to check: "))
##
##if n < 0:
##    print("This is negative number", n)
##
##elif n == 0:
##    print("The number is zero", n)
##
##else:
##    print("Number is Positive", n)


##Ques : 19

##n = 25
##
##if n % 2 == 0:
##    print("Even Number")
##
##else:
##    print("Odd number")


##Ques : 20

##def calculate_square(n):
##    print("Square : ",n ** 2)
##
##calculate_square(5)


## SECTION D

##Ques : 21

##n = int(input("Enter marks: "))
##
##if n >= 90 and n < 100:
##    print(f'Marks : {n} Grade : A')
##
##elif n >= 75 and n < 89:
##    print(f'Marks : {n} Grade : B')
##
##elif n >= 60 and n < 74:
##    print(f'Marks : {n} Grade : C')
##
##elif n >= 40 and n < 59:
##    print(f'Marks : {n} Grade : D')
##
##else:
##    print(f'Marks : {n} Grade : E')

##Ques : 22

##
##n = int(input("Enter a number: "))
##
##if n > 0:
##    if n % 2 == 0:
##        print("Positive Even Number")
##
##    else:
##        print("Positive Odd Number")
##
##elif n < 0:
##    if n % 2 == 0:
##        print("Negative Even number")
##
##    else:
##        print("Negative Odd number")
##
##else:
##    print("0")