try:
    num1,num2=(eval(input("Enter two numbers, seperated by a comma:")))
    result= num1/num2
    print("result is",result)

except ZeroDivisionError:
    print("Division by zero is error")

except SyntaxError:
    print("Comma is missing. Enter with comma(1,2)")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("This will execute no matter what")