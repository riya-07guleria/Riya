for i in range(3):
    age= int(input("Enter your age:"))
    if age>= 21:
        print("You are eligible for marriage.")
    elif 18<= age < 21:
        print("You are almost eligible. Just wait a bit more!")
    else:
        print("Too young for marriage.")