def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = int(input('Enter the no:'))
print(f"Sum of digits: {sum_of_digits(n)}")
#write a program to find the sum of digits of a given number'
