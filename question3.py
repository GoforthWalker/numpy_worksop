num = int(input('Enter the num value:'))
factorial = 1

if num < 0:
    print("num is negative")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i

    print(f"The factorial of {num} is {factorial}")
#write a program to find the factorial of a nummber
