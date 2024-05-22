num = int(input('Enter the num value:')) 

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            print(f"{i} times {num // i} is {num}")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
#write a program to find if the given number is prime no or not
