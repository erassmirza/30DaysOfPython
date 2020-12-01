""" Exercises """

"""
# 1
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 2
print('Coding' + ' ' + 'For' + ' ' + 'All')
"""

# 3
company = 'Coding For All'

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[:6])

# 10
print(company.index('Coding'))
print(company.find('Coding'))
print(company.rindex('Coding'))
print(company.rfind('Coding'))
print(company.startswith('Coding'))

# 11
print(company.replace('Coding','Python'))

# 12
print('Python for Everyone'.replace('Everyone','All'))

# 13
print(company.split())

# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# 15
print(company[0])

# 16
print(company.rfind('l'))

# 17
print(company[10])

# 18
print('Python For Everyone'.replace('Python For Everyone','PFE'))

# 19
print(company.replace('Coding For All','CFA'))

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
print('Coding For All People'.rfind('l'))

# 23
sen = 'You cannot end a sentence with because because because is a conjunction'
print(sen.find('because'))

# 24
print(sen.rfind('because'))

# 25
print(sen.replace('because because because ',''))

# 26
print(sen.find('because'))

# 27
print(sen.replace('because because because ',''))

# 28
print(company.startswith('Coding'))

# 29
print(company.endswith('coding'))

# 30
print('   Coding For All      '.strip())

# 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\t\tAge\tCountry\nAsabeneh\t250\tFinland')

# 35
radius = 10
area = 3.14 * radius ** 2
print(f'''
radius = {radius} 
area = 3.14 * radius ** 2
The area of a cricle with radius {radius} is {area} meters square.
''')

# 36
first_num, second_num = 8,6
print(f'''
{first_num} + {second_num} = {first_num + second_num}
{first_num} - {second_num} = {first_num - second_num}
{first_num} * {second_num} = {first_num * second_num}
{first_num} / {second_num} = {first_num / second_num}
{first_num} % {second_num} = {first_num % second_num}
{first_num} // {second_num} = {first_num // second_num}
{first_num} ** {second_num} = {first_num ** second_num}
''')