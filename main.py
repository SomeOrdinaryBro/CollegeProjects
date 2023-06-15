def Circle():
    print(" ")
    print("Select an opration to Perform")
    print(" ")
    print("1.Diameter")
    print("2.Circumference")
    print("3.Area")
    print(" ")
    choice = input("Enter Your choice [1/2/3]: ")

    if choice in ('1', '2', '3'):

        if choice == '1':
            PI = 3.14
            radius = float(input(' Please Enter the radius of a circle: '))

            diameter = 2 * radius
            print(" \nDiameter Of a Circle = %.2f" % diameter)

        elif choice == '2':
            PI = 3.14
            radius = float(input(' Please Enter the radius of a circle: '))

            circumference = 2 * PI * radius
            print(" Circumference Of a Circle = %.2f" % circumference)

        elif choice == '3':
            PI = 3.14
            radius = float(input(' Please Enter the radius of a circle: '))

            area = PI * radius * radius
            print(" Area Of a Circle = %.2f" % area)


def Square():
    print(" ")
    print("Select an opration to Perform")
    print(" ")
    print("1.Perimeter")
    print("2.Area")
    print(" ")
    choice = input("Enter Your choice [1/2]: ")

    if choice in ('1', '2'):

        if choice == '1':
            s = int(input("How Many Sides Does Your Squre Have : "))
            area = s * s
            print("Area of Square : ", area)

        elif choice == '2':
            s = int(input("How Many Sides Does Your Squre Have : "))
            perimeter = 4 * s
            print("Perimeter of Square : ", perimeter)


def Rectangle():
    print(" ")
    print("Select an opration to Perform")
    print(" ")
    print("1.Perimeter")
    print("2.Area")
    print(" ")
    choice = input("Enter Your choice [1/2]: ")

    if choice in ('1', '2'):

        if choice == '1':
            l = int(input("Length : "))
            w = int(input("Width : "))
            area = l * w
            print("Area of Rectangle : ", area)

        elif choice == '2':
            l = int(input("Length : "))
            w = int(input("Width : "))
            perimeter = 2 * (l + w)
            print("Perimeter of Rectangle : ", perimeter)


while True:
    print(".......................................")
    print("Select A Shape to Perform Calculation's")
    print(".......................................")
    print(" ")
    print("1.Circle")
    print("2.Square")
    print("2.Rectangle")
    print(" ")

    choice = input("Enter Your choice [1/2/3] : ")

    if choice in ('1', '2', '3'):

        if choice == '1':
            Circle()

        elif choice == '2':
            Square()

        elif choice == '3':
            Rectangle()

        next_calculation = input("Would You Like To Do Another Calculation? (YES/NO): ")
        if next_calculation == "NO":
          break
        if next_calculation == "no":
          break
    
        else:
          print("Invalid Input")