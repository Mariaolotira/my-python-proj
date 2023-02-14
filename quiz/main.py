#number=int(input("Enter a number from 1 to 100"))
for number in range(100):
    if number % 3 ==0 and number % 5==0:
        print(number, "fizzBuzz")
    elif number % 3 ==0:
        print(number, "fizz")
    elif number % 5 ==0:
        print(number, "Buzz")



