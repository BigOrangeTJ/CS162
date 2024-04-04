
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))
def rect_area(length, width):
    return length * width

rect_area = rect_area(length, width)

print("Lenth = ", length, "Width = ", width)
print("Rectangle Area = ", rect_area)

def rect_solid_area(lenth, width, height):
    '''Take inputs from user and calculate surface area'''
    '''This function written by Brian S.'''
    return rect_area * 2 + lenth * height * 2 + height * width * 2

surface_area = rect_solid_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)

