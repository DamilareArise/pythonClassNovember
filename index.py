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

"""

# num = 10 + 3j
# print(type(num))

basket = ('Pepper', 'fish', 'rice')
# print(type(basket))

# range10 = range(1, 10, 3)
# print(list(range10))

isMarried = False
print(type(isMarried))