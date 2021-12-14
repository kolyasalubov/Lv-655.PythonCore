import slide_45_1

print('''Which square do you want to calculate?
If you need to find the square of rectangle push 1
If you need to find the square of triangle push 2
If you need to find the square of circle push 3''')

a = int(input())

if a == 1:
    side_1 = int(input())
    side_2 = int(input())
    print(slide_45_1.square_of_rectangle(side_1, side_2))
elif a == 2:
    height = int(input())
    side_1 = int(input())
    print(slide_45_1.square_of_triangle(height, side_1))
elif a == 3:
    radius = int(input())
    print(slide_45_1.square_of_circle(radius))
