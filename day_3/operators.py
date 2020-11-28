""" Exercises: Level 1 """


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