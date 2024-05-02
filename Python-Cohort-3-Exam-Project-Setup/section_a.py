# (a)(i)
def calculateGrades():
    print("\n.Student Grade Calculations.")

    #capture student mark
    mark = int(input('Enter the mark scored by the student:\t'))
    
    #student mark
    if mark>=90 and  mark<=100:
        print("Grade is A")

    elif mark>=80 and mark<=89:
        print("Grade is B")

    elif mark>=70 and mark<=79:   
        print("Grade is C") 

    elif mark>=60 and mark<=69:   
        print("Grade is D")   

    elif mark>=50 and mark<=59:   
        print("Grade is E")  

    else:
        print("Fail")  
        
# calling the function
calculateGrades()

    

#(a)(ii)
def temperatureConvert():
    option = int(input("Select your choice (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius Degrees: "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")

    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit Degrees: "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid option!") 
        print("Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius ")
        
# calling the function
    temperatureConvert()

# #(b)(i)
def calculate_triangle_area(base, height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = calculate_triangle_area(base, height)
print(f"The area of the triangle is: {area}")



# #(b)(ii)
def sum_of_items():
    numbers = [9,2,3,5,8]
    sum = 0

    for number in numbers:
        sum += number
    print("The sum of items in the list is: " + str(sum))  
    
# calling the function
sum_of_items()
