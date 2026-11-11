while True:
    first_number=float(input("enter your first number:"))
    operation=input("enter your operation(+,-,*,/,%)")
    second_number=float(input("enter your second number:"))
    if operation=="+":
        result=first_number+second_number
    elif operation=="-":
         result=first_number-second_number
    elif operation=="*":
        result=first_number*second_number
    elif operation=="**" and second_number!=0:
        result=first_number**second_number
    elif operation=="/"and second_number!=0:
        result=first_number/second_number
    elif operation=="%":
        result=first_number%second_number
    elif operation=="/" or operation=="%":
        print("cannot dividely zero!")
        continue
    else:
        print("invalid operation!")
        continue
    print(f"{first_number}{operation}{second_number}={result}")
    again=input("do you want to calculator again?(no/yes):")
    if again=="no":
     print("goodbye!")
     break