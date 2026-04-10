print("Welcome to Pattern Generator and Number Analyzer !")


while True :

    menu = int(input("""\n\n Select an option : \n
                    1. Right Angle Triangle Shape
                    2. Reverse Right Angle Triangle Shape
                    3. Left Angle Triangle Shape
                    4. Reverse Left Angle Triangle Shape
                    5. Pyramid Angle Shape
                    6. Reverse Pyramid Angle Shape
                    7. Diamond Shape 
                    8. Number Analyzer 
                    9. Exit \n
                    Enter your choice : """))


    if ( menu == 1 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( 1 , rows + 1 ) :
            print("*" * i)


    elif ( menu == 2 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( rows , 0 , -1 ) :
            print("*" * i)


    elif ( menu == 3 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( 1 , rows + 1 ) :
            print(" " * ( rows - i ) + "*" * i)


    elif ( menu == 4 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( rows , 0 , -1 ) :
            print(" " * ( rows - i ) + "*" * i)


    elif ( menu == 5 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( 1 , rows + 1 ) :
            print(" " * ( rows - i ) + "*" * ( 2 * i - 1 ))


    elif ( menu == 6 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( rows , 0 , -1 ) :
            print(" " * ( rows - i ) + "*" * ( 2 * i - 1 ))


    elif ( menu == 7 ) :

        rows = int(input("\n\t\t    Enter the number of rows : "))

        for i in range ( 1 , rows + 1 ) :
            print(" " * ( rows - i ) + "*" * ( 2 * i - 1 ))

        for i in range ( rows - 1 , 0 , -1 ) :
            print(" " * ( rows - i ) + "*" * ( 2 * i - 1 ))


    elif ( menu == 8 ) :

        total = 0

        start = int(input("\n\t\t    Enter the Number from Start : "))
        end = int(input("\n\t\t    Enter the Number to end : "))

        for i in range ( start , end + 1 ) :
            if ( i % 2 == 0 ) :
                print(i , ": Even") 
            else :
                print(i , ": Odd")

            total += 1


    elif ( menu == 9 ) :
        print("Thank you !...")
        break


    else : 
        print("Please enter the valid number !...")