choice = int(input("Which operator do you plan to use? addition {1}; subtraction {2}; multiplication {3}; division {4}: "))
if choice == 1:
    sum1 = float(input("First term of the sum: "))
    sum2 = float(input("Second term of the sum: "))
    sum3 = sum1 + sum2
    print("Sum:", sum3)
elif choice == 2:
    sub1 = float(input("Total value for the subtraction: "))
    sub2 = float(input("Value to be subtracted:: "))
    sub3 = sub1 - sub2
    print("Subtraction result:", sub3)
elif choice == 3:
    mult1 = float(input("First factor in the multiplication: "))
    mult2 = float(input("Second number in the multiplication: "))
    mult3 = mult1 * mult2
    print("Product of the multiplication:", mult3)
elif choice == 4:
    div1 = float(input("Dividend (total amount to be divided): "))
    div2 = float(input("Divisor (the number to be divided by): "))
    try:
        div3 = div1 / div2
        print("Result of the division:", div3)
    except ZeroDivisionError:
        print("You cannot divide by zero")