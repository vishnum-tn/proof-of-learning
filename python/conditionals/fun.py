def main():
    x = int(input("Enter the first number: "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
def is_even(x):
    return True if x % 2 == 0 else False
#we can use and return two line of code in the one line above code is the example of the one line of code.

main()