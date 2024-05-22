def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))

n = int(input("Enter an integer: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
# find if the given number is a palindrome or not?
