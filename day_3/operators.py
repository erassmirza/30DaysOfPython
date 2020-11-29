""" Exercises """


# 1
my_age = 22

# 2
my_height = 5.7

# 3
complex_num = 2+4j

# 4
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area_of_triangle = int(0.5 * base * height)
print('The area of the triangle is',area_of_triangle)

# 5
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is',perimeter)

# 6
length_of_rec = int(input('Enter length of Rectangle: '))
width_of_rec = int(input('Enter width of Rectangle: '))
area_of_rec =  length_of_rec * width_of_rec
perimeter_of_rec = 2 * (length_of_rec + width_of_rec)
print('Area of Rectangle is',area_of_rec)
print('Perimeter of Rectangle is',perimeter_of_rec)

# 7
pi = 3.14
radius_of_circle = int(input('Enter radius of Circle: '))
area_of_circle = pi * radius_of_circle ** 2
circum_of_circle  = 2 * pi * radius_of_circle
print('Area of Circle is',area_of_circle)
print('Circumference of Circle is',circum_of_circle)

# 8
x = 0
y = 2 * x - 2
print('y-intercept is',y)
y = 0
x = (y + 2) / 2
print('x-intercept is',x)
m1 = 2
print('y = 2 * x - 2 compare with y = m * x + b so slope is',m1)

# 9
x1,y1,x2,y2 = 2,2,6,10
m2 = (y2 - y1) / (x2 - x1)
print("Slope 'm' is",m2)

# 10
print('Slopes in tasks 8 and 9 are same:',m1 == m2)

# 11
x = [1,-1,2,-2,3,-3]
y = x[0] ** 2 + 6 * x[0] + 9
print('When x is 1 value of y is:',y)
x = [1,-1,2,-2,3,-3]
y = x[1] ** 2 + 6 * x[1] + 9
print('When x is -1 value of y is:',y)
x = [1,-1,2,-2,3,-3]
y = x[2] ** 2 + 6 * x[2] + 9
print('When x is 2 value of y is:',y)
x = [1,-1,2,-2,3,-3]
y = x[3] ** 2 + 6 * x[3] + 9
print('When x is -2 value of y is:',y)
x = [1,-1,2,-2,3,-3]
y = x[4] ** 2 + 6 * x[4] + 9
print('When x is 3 value of y is:',y)
x = [1,-1,2,-2,3,-3]
y = x[5] ** 2 + 6 * x[5] + 9
print('When x is -3 value of y is:',y)

# 12
print("Length of 'python' and 'jargon' is not same:",len('python') != len('jargon'))

# 13
print("'on' is present in python and jargon:",'on' in 'python' and 'on' in 'jargon')

# 14
check_jargon = 'jargon' in 'I hope this course is not full of jargon'
print("jargon is presnt in this sentence 'I hope this course is not full of jargon':",check_jargon)

# 15
print("There is no 'on' in both dragon and python:",'on' not in 'dragon' and 'on' not in 'python')

# 16
length_of_python = len('pyhton')
print('Length of python in float:',float(length_of_python))
print('Length of python in string:',str(length_of_python))

# 17
even_num = int(input('Enter the number: '))
print('Your number is even:',even_num % 2 == 0)

# 18
print('floor division of 7 by 3 is equal to the int converted value of 2.7:',7/3 == int(2.7))

# 19
print("type of '10' is equal to 10:",type('10') == 10)

# 20
print("int('9.8') is equal to 10:",int(9.8) == 10)

# 21
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earning = hours * rate_per_hour
print('Your weekly earning is',weekly_earning)

# 22
number_of_years = int(input('Enter number of years you have lived: '))
lived_years = number_of_years * 365 * 24 * 60 * 60
print('You have lived for',lived_years,'seconds.')

# 23
num1,num2,num3,num4,num5 = 1,2,3,4,5
print(num1,num1,num1,num1,num1)
print(num2,num1,num2,num2 ** 2,num2 ** 3)
print(num3,num1,num3,num3 ** 2,num3 ** 3)
print(num4,num1,num4,num4 ** 2,num4 ** 3)
print(num5,num1,num5,num5 ** 2,num5 ** 3)