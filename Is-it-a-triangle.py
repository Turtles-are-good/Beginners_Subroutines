def is_triangle(side_a, side_b, side_c):
    return side_a + side_b > side_c

a = int(input("Enter the smallest side of your shape"))
b = int(input("Enter the second smallest side of your shape"))
c = int(input("Enter the largest side of your shape"))

test = is_triangle(a, b, c)
if is_triangle(a, b, c) :
    print(a, "+", b, ">", c, "so this shape is a triangle")
else :
    print(a, "+", b, "<=", c, "so this shape is not a triangle")