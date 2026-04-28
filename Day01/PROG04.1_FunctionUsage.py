#PROG 04.1 : Function Usage

#Global Variable
pi=3.14

#function to calculate area of circle
def area_of_circle(radius):
    area=pi*radius*radius #area formula
    return area

#function to calculate circumference of circle
def circumference_of_circle(radius):
    circumference=2*pi*radius #circumference formula
    return circumference

#taking value of radius from user
r=float(input("Enter the radius of the circle: "))
#calling area function
area=area_of_circle(r)
#calling circumference function
circumference=circumference_of_circle(r)
#printing area and circumference
print("Area of the circle: ", area)
print("Circumference of the circle: ", circumference)

