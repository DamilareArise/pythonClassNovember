# print('Welcome to python class...')

# Types of commenting
# 1. This is a single line comment
"""
2. This is a multiline comment
"""

# print(''' 

#     My name is Damilare.
#     I am a python dev;  
#     ''')

# Python variable

# person = "Mr Sayo"
# occupation = "Python Dev"
# amount = 5000

# newAmount = amount + 2000

# value1 = 20
# value2 = 30
# print(value1 + value2)

# concatenation -> process of joining two or more strings together
# print(person + occupation)
# print(person,occupation)

# print(person +' has upto #'+str(newAmount))
# print(f"{person} has upto #{newAmount}")
# rules guiding variable declaration
"""
1. A variable name must be descriptive
2. It can only start with alphabet or underscore,
3. It does not allow space inbetween words, rather you can use;
    i. snake casing e.g the_first_child_in_the_family
    ii. camel casing e.g theFirstChildInTheFamily
    iii. pascal casing e.g TheFirstChildInTheFamily
4. A variable name only allows alphabet, underscore and number
5. Don't use python key Words
"""

# first_name = input("Firstname: ")
# print(f"Welcome {first_name}")

# Types of variable declaraton
# 1. Single variable single value declaration
x = 10
# 2. single variable multiple value
x = 10, 20, 30, 40, 50
# print(x)
# 3. multiple variable single value declaration
x = y = z = 20
# 4. multiple variable multiple value declaration
# x, y, z = 10, 20, 30
firstname, lastname, age = 'Damilare', 'Arise', 20
# print(f'My name is {firstname} {lastname}. I am {age}years old.')


# Python data types
"""
1. Strings  str() e.g "Hello, world"
2. Number Type;
    i. integers int() e.g 10, 20, 30
    ii. float float() e.g 10.5, 20.5, 30.5
    iii. complex complex() e.g 10+20j, 20+30j
3. Sequence Type;
    i. list list() e.g [1, 2, 3, 4, 5]
    ii. Tuple tuple() e.g (1, 2, 3, 4, 5)
    iii. range range() e.g range(1, 10)
4. Boolean Type bool() e.g True, False
5. Mapping Type; dict() e.g {'name': 'Damilare', 'age': 20}
6. Set type; set() e.g {'Ade',  'Segun'}
7. binary type; byte, bytearray, memoryview
"""

# num = 10 + 3j
# print(type(num))

basket = ('Pepper', 'fish', 'rice')
# print(basket[-1])
# print(type(basket))

# range10 = range(1, 10, 3)
# print(list(range10))

# isMarried = False
# print(type(isMarried))

student = {
    "name": 'Damilare',
    'course': 'Datascience',
    'isGraduate': True,
    'grade': 4.0,
    'amount': 40000
}
# print(student['grade'])
# print(f'Amount is #{student['amount']}')


# if student['grade'] > 3:
#     print('You are a good student')
# else:
#     print('You are a bad student')

# student = {'ade', 'segun', 'lola', 'femi'}
# score = {12, 13, 14, 11, 15}
# print(score)

# print(ord('o'))
# print(chr(97))

# var = 'Hello' # ['H', 'e' , 'l' , 'l', 'o']
# print(var[-1])

# var = bytes([72, 101, 108, 108, 111])
# print(var)

students = ['Yemi', 'Dare'] # [['Y', 'e', 'm', 'i'], ['D', 'a', 'r', 'e']]
# print(students[0][3])


# Python Operators
'''
1. Arithmetic Operator: +, -, *, /, %, //, **
2. Assignment operator: =, +=, -=, *=, /=, %=, //=, **=
3. Comparison Operator: ==, !=, >, <, >=, <=
4. Logical Operator: and, or, not
5. Identity Operator: is, is not
6. Membership Operator: in, not in


AND Operator
A ____ B _____Output
T ____ T _____ T
T ____ F _____ F
F ____ T _____ F
F ____ F _____ F

OR Operator
A ____ B _____Output
T ____ T _____ T
T ____ F _____ T
F ____ T _____ T
F ____ F _____ F

Not Operator
A ____ Output
T ____ F
F ____ T

'''
# print(5 ** 2)

x = 4
# x-=1 
# print(x <= 5)

# conditional statement

# if x > 5:
#     print('Yes')
# elif x == 5:
#     print('x is equal 5')
# else:
#     print('No')

'''
0 - 39 -> F
40 - 44 -> E
45 - 49 -> D
50 - 59 -> C
60 - 69 -> B
70 - 100 -> A

'''

# score = int(input('Input your score: '))
# if score >= 70 and score <=100:
#     print('A')
# elif score >=60 and score <=69:
#     print('B')
# elif score >= 50 and score <= 59:
#     print('C')
# elif score >= 45 and score <= 49:
#     print('D')
# elif score >= 40 and score <= 44:
#     print('E')
# elif score >= 0 and score <= 39:
#     print('F')
# else:
#     print('Invalid score')
    
    
# print('Welcome to MyCalc App')
# value1 = float(input('First Value: '))
# value2 = float(input('Second Value: '))
# print('''
#       1. Addition
#       2. Subtraction
#       3. Multiplication
#       4. Division
#       #. Exit
#     ''')
# user_choice = input('Enter your choice: ')
# if user_choice == '1':
#     result = value1 + value2
#     print(f'Your answer is {result}')
# elif user_choice == '2':
#     result = value1 - value2
#     print(f'Your answer is {result}')

# else:
#     print('Invalid choice')
    
    
# val = 5
# val2 = 4
# print(val is not val2)

# fruits = ['Banana', 'Mango', 'Orange']
# print('banana' not in fruits)


# balance = 20
# if balance > 0:
#     option = input('press 1 to play game or # to exit: ')
#     if option == '1':
#         print('playing game...')
        
#     elif option == '#':
#         print('goodbye...')
#         exit()
#     else:
#         print('invalid option')
# else:
#     print('Insufficient balance')
    
# print('I am still here')


# food_available = [
#     'Rice',
#     'Beans',
#     'Yam Porridge',
#     'Amala',
#     'Fufu'
# ]

# compliment = [
#     'Fish',
#     'Egg',
#     'Meat'
# ]

# user_food = input(f'''
#              Avaliable foods :-> {food_available} 
             
#              Place order; ''')

# user_compliment = input(f'''
#              Avaliable compliments :-> {compliment} 
             
#              Place order; ''')

# if user_food in food_available and user_compliment in compliment:
#     print('Proceed to make payment, Order available.')
# elif user_food in food_available:
#     print('Compliment ordered not avaliable. Choose another or cancel order')
# elif user_compliment in compliment:
#     print('Food ordered not avaliable. Choose another or cancel order')
# else:
#     print('Order not avaliable')


# Python Strings
# var = 'Hello, Welcome to the to 2nd week, in python class.'
# name = '123'
# print(type(var))
# print(len(var))
# print(var.upper())
# print(var.lower())
# print(name.capitalize())
# print(var.title())

# print(var[10:20]) #slicing 

# list_var = var.split(',')
# print(len(list_var))
# print(list_var)

# list_item = ['Apple', 'Orange', 'Tomato']
# print(' is '.join(list_item))

# print(name.startswith('D'.lower()))
# print(var.endswith('class.'))

# print(var.count('to'))
# print(var.find('to', 10, -1))

# print(name.isnumeric())



# score = 0
# question1 = input('What is the capital of Osun state a. Abeokuta b. Ibadan c. Osogbo : ')
# if question1.strip().upper() == 'C':
#     print('Correct') 
#     score +=5
# else:
#     print('Wrong')
    
# print(f'score is {score}/5')


# Word counter
# expression = input('Input your sentence: ')
# list_exp = expression.strip().split()
# print(f'The word count is {len(list_exp)}')
# print(len(expression))

# escape characters
'''
\n -> next line
\t -> tab
\r -> return
\\ -> backslash
\' -> single quote

'''

# text = r'Hello, my name is \t\tJohn Doe. it\'s mine'
# print(text, end='\t')

# path = r'E:\All_Python\novemberCohort\index.py'
# # r -> raw string
# print(path)


# Python Collections/Array
# 1. LIST: list() or []. a list object is ordered, changeable/immutable, indexed, and allows duplicate value

students = [
    'Ade Thomas',
    'Ola Kings',
    'John Doe',
    'Femi Badmus',
    'John Adams'
] 

# print(students[0])
# print(students[-3])
# print(students[0:3]) #slicing
# print(students[::-1]) #reverse order

# students[0] = 'Adeola'
# print(students)


# students.append('Shola')
# students.extend(['Shola', 'Dami']) 
# students.insert(0, 'Shola')

# students.pop(2)
# students.remove('john')
# students.clear()
# del students[0]

numbers = [3, 2, 5, 6, 4, 7, 8, 1, 9]

# numbers.sort(reverse=True)
# print(numbers)

# students.sort(key=len)
# print(students)  # sort by length of names


# for loop

# print(f'{students[0]} is a student ')
# print(f'{students[1]} is a student ')
# print(f'{students[2]} is a student ')
# for stud in students:
#     print(f'{stud} is a student ')


# register students
# students = []
# user = int(input('No of students: '))

# for i in range(user):
#     name = input(f'Student{i+1} Name: ')
#     students.append(name)

# print(students)

# for i in range(1 ,11):
#     print(i)
#     print('_______')

# [1, 2, 3...,10]

questions = [
    'What is the capital of Osun state a.) Ibadan b.) Oshogbo',
    'What is the capital of Oyo state a.) Ibadan b.) Oshogbo',
    'What is the capital of Lagos state a.) Ibadan b.) Ikeja'
]

answers = [
    'b',
    'a',
    'b'
]
# score = 0

# for ques, ans in zip(questions, answers):
#     print(ques)
#     user = input('Answer: ')
#     if user.strip().lower() == ans:
#         score += 1
#         print('Correct✅')
#     else:
#         print('Wrong❌')
    
    
# print(f'You scored {score}/{len(questions)}')


# numbers = [3, 2, 5, 6, 4, 7, 8, 1, 9]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# mean = sum(numbers)/len(numbers)
# print(mean)

items = [
    'Toothpaste',
    'Milk',
    'Bath Soap'
]

prices = [
    100,
    200,
    150
]


# for item, price in zip(items, prices):
#     print(f'{item} is sold for #{price}')

students = [
    'Ade Thomas',
    'Ola Kings',
    'John Doe',
    'Femi Badmus',
    'John Adams'
] 

questions = [
    'What is the capital of Osun state a.) Ibadan b.) Oshogbo',
    'What is the capital of Oyo state a.) Ibadan b.) Oshogbo',
    'What is the capital of Lagos state a.) Ibadan b.) Ikeja'
]

answers = [
    'b',
    'a',
    'b'
]

marks = [
    2,
    3, 
    1
]



# for student in students:
#     print(f'{student} it is time for your exam.! \n')
#     score = 0
#     for ques, ans, mark in zip(questions, answers, marks):
#         print(ques)
#         user = input('Answer: ')
#         if user.strip().lower() == ans:
#             score += mark
#             print('Correct✅')
#         else:
#             print('Wrong❌')
    
    
#     print(f'{student} scored {score}/{len(questions)} \n\n')
    
    
# Assignment 
'''
Build a CBT application that would perform the following functionality;
1. Ask the user for the amount of student taking the test
2. register all the student
3. ask the user for the number of questions
4. allow the user to create the queestions and the equivalent answers base n the number of questions
5. call the students one after the other to take the test
6. print out the student with the highiest score and lowest score
7. print out the mean score.
'''

# 2. Tuple: () or tuple(). It is a collection method that is  ordered, indexed, allows duplicate value but unchangeable/mutable

emails = (
    'femi@gmail.com',
    'john@gmail.com',
    'john@gmail.com',
    'mercy@gmail.com'
)
# print(emails[0:2])

# emails[0] = 'ade@gmail.com' #'tuple' object does not support item assignment
# print(emails.count('john@gmail.com'))
# print(emails.index('femi@gmail.com'))

emails_list = list(emails)
emails_list[0] = 'ade@gmail.com'
# print(emails_list)

# emails = tuple(emails_list)
# print(emails)

# unpacking
# *all, = emails
# print(all)

first, *all, last = emails
# print(all)


# questions_answers = [
#     ('What is the capital of Osun state a.) Ibadan b.) Oshogbo', 'b', 5),
#     ('What is the capital of Oyo state a.) Ibadan b.) Oshogbo', 'a', 10),
# ]

# score = 0
# for quest, ans, other in questions_answers:
#     print(quest)
#     user = input('answer: ')
#     if user == ans:
#         score += other
        


# 3, set: {}, set(): It is a collection method that is unordered, unindexed, no duplicate value and mutable

names = {
    'femi',
    'john',
    'john',
    'mercy',
    'ola',
    'ade'
}

# *all, = names
# print(all)


# names.add('ola')
# names.update(['ola', 'yemi'])
# names.remove('John') 
# names.discard('John')
# print(names.pop())
# print(names)

# names = [
#     'femi',
#     'john',
#     'mercy',
#     'ola',
#     'ade'
# ]
# for num, name in enumerate(names, start=1):
#     print(f"{num}.) {name}")

# x = 16
# for name in names:
#     print(x, name)
#     x+=1
    

# guess = set(names).pop()
# user = input('Your guess: ')
# if user == guess:
#     print('You won')
# else:
#     print('You lost')
    


# numbers_str = [ str(num) for num in range(100)]
# for num in range(100):
#    numbers_str.append(str(num))

# print(set(numbers_str))

# random_numbers = []
# set_numbers_str = set(numbers_str)
# for x in range(10):
#    random_numbers.append(set_numbers_str.pop())    
   
# print(random_numbers)

# print('Guess 3 numbers that would be part of our selected numbers between 0-100')
# user_guesses = []
# for i in range(3):
#     user = input('Your guess: ')
#     user_guesses.append(user)
    
    
# print(random_numbers)
# print(user_guesses)

# if set(user_guesses).issubset(set(random_numbers)):

# if any([guess in random_numbers for guess in user_guesses ]):
#     print('You won')
# else:
#     print('You lost')





# print(any([0 , False, None]))


# numbers = [i for i in range(5) ]  #List Comprehension
# for i in range(5):
#     numbers.append(i)
    
# print(numbers)


# names = [ input(f'Name{i}: ') for i in range(3) ]

# for i in range(3):
#     name = input('Name: ')
#     names.append(name)
# print(names)



setA = {3, 4, 2, 1, 6, 7, 9, 8, 0, 5}
setB = {3, 4, 7, 0}
setC = {11, 14, 12, 10, 3, 5}

# new_set =  setA.union(setC)
# new_set =  setA.intersection(setC)
# new_set =  setA.difference(setC)
# new_set =  setA.symmetric_difference(setC)
# print(new_set)

# setA.intersection_update(setB)
# setA.difference_update(setB)
# print(setA)

# setA.update(setC)
# print(setA)

# print(setA.issuperset(setB))
# print(setB.issubset(setA))
# print(setA.isdisjoint(setC))


# students = [
#     'ade',
#     'ola',
#     'femi'
# ]

# scores = [
#     23,
#     34,
#     12
# ]

# max_score = max(scores)
# ind_max_score = scores.index(max_score)

# student_max = students[ind_max_score]


# 4. Dictionary: {key:value}, dict(key=value); it is ordered, it doesnt allow duplicate key, it is changeable.
 
car = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2015,
    'color': 'blue',
    'owner': {
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'state': 'NY'
        }
    }
}


# print(car['color'])
# car['years'] = 2018
# print(car)

# print(car['owner']['address']['city'])

# for key in car.keys():
#     print(key)

# print(car.values())
# print(car.items())

# for key , value in car.items():
#     print(f'{key} => {value}')


# questions = {
#     'What is the capital of Osun state a.) Ibadan b.) Oshogbo' :'a',
#     'What is the capital of Oyo state a.) Ibadan b.) Oshogbo' : 'b',
#     'What is the capital of Lagos state a.) Ibadan b.) Ikeja' : 'b'
# }

# for ques, ans in questions.items():
#     print(ques)
#     user = input('Answer: ')
#     if user == ans:
#         print('Correct')
#     else:
#         print('Wrong')

# print(car.get('model', 'Invalid key') )
# car.update({'registered': False})
# print(car.pop('years', 'Invalid key'))
# car.clear()
# car['model'] = 'Benz'
# print(car)

[]

[
    {},
    {}
]

# students = []
# for i in range(3):    
#     student = {
#         'name': input('Name: '),
#         'matNo': input('Matric No: '),
#         'score': 0
#     }
#     students.append(student)

# print(students)

{
    'id1':{},
    'id2': {}
}

# students = dict()

# for i in range(3):
#     student = {
#         'name': input('Name: '),
#         'score': 0
#     }
#     # students.update({f'00{i+1}': student})
#     students[f'00{i+1}'] = student
    
# print(students)

# JSON -> JavaScript Object Notation
[],
{},
[{}]
# API -> Application Programming Interface

# import requests

# url = "https://fakestoreapi.com/products/"
# response = requests.get(url)
# data = response.json()
# print(data[0])
# for key, value in data[0].items():
#     print(f'{key} => {value}')

# product_names = []
# product_prices = []
# names_prices_obj = {}
# for each in data:
    # print(each['title'])
    # product_names.append(each['title'])
    # product_prices.append(each['price'])
    # names_prices_obj[each['title']] = each['price']
    
# ind_max = product_prices.index(max(product_prices)) 
# print(product_names[ind_max], product_prices[ind_max])

# print(max(names_prices_obj, key=names_prices_obj.get))

# data = {
#     'ade': 20,
#     'ola': 30,
#     'femi': 40
# }
# print(max(data, key=data.get))



# While loop 

# x = 10
# while x > 0:
#     print(x)
    
#     x-=1

# x = 0
# while x < 10:
#     print(x)
#     x+=1

# x = 5

# while x > 0 and x < 15:
#     print(x)
#     x-=1


# ticket =  10
# while ticket > 0:
#     age = int(input('Age: '))
#     if age < 18:
#         print('You are not eligible!')
#         continue
    
#     ticket-=1
#     print('Total ticket is ', ticket)


students = []

# while True:
#     student = {
#         'fullname': input('Enter your name: '),
#         'matNo': input('Enter your matric no: ')
#     }
#     students.append(student)
#     user = input('Press enter to continue registration or 1 to stop: ')
#     if user != '1':
#         continue
#     else:
#         break
    
# print(students)


# ussd = input('ussd code: ')
# while ussd != '*312#':
#     print('Invalid ussd code')
#     ussd = input('ussd code: ')
#     continue

# print('Valid ussd code')


# PYTHON FUNCTION
'''
1. Declaration  Stage (Naming)
2. Definition Stage (performance)
3. Invocation Stage (calling)

'''
# def dance():
#     print('I am dancing')

# dance()


def addition():
    val1 = float(input('Value 1: '))
    val2 = float(input('Value 2: '))
    result = val1 + val2
    print(f'Ans = {result}')
    proceed()
    
def subtraction():
    val1 = float(input('Value 1: '))
    val2 = float(input('Value 2: '))
    result = val1 - val2
    print(f'Ans = {result}')
    proceed()
    
def multiply():
    val1 = float(input('Value 1: '))
    val2 = float(input('Value 2: '))
    result = val1 * val2
    print(f'Ans = {result}')
    proceed()
    
def proceed():
    user = input('Press enter to continue or 1 to exit: ')
    if user != '1':
        home()
    else:
        print('Exiting...')
        exit()
    
def home():
    print('''
          
        My Calculator
        
        1. Addition
        2. Subtraction
        3. Muplication
        #. Exit
    ''')
    user = input('Input your choice: ').strip()
    if user == '1':
        addition()
    elif user == '2':
        subtraction()
    elif user == '3':
        multiply()
    elif user == '#':
        print('Exit')
        exit()
    else:
        print('Invalid choice')
        home() #Recurssive function

home()


