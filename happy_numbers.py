def is_happy_number(n):
    seen = set()  
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  
    return n == 1

# Input from user
number = int(input("Enter the number: "))
if is_happy_number(number):
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.") 

    