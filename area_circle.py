#Contribution: new function to perform area of a circle.
PI = 3.14

def area_circle():
    user_r = int(input("Please enter a radius: "))
    area = PI * user_r**2

    return f"Area of cricle: {area}"