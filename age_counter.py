try:
    age=int(input("Enter age:"))
    if age%2==0:
        print("even number")
    else:
        print("odd number")
except ValueError:
    print("invalid input")
    