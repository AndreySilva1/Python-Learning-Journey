try:
    integer_number = int(input("Enter an integer number: "))

    if integer_number % 2 == 0:
        print("The number you entered is even!")
    else:
        print("The number you entered is odd!")
except:
    print("The value you entered is not an integer!")
