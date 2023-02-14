try:
    def age():
        your_age = int(input("Enter your age"))
        month = 12
        total = your_age*month
        print("You have lived for {total} months")


    age()
except:
    print("Not a number")
