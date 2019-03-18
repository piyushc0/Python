# 0 means Success
# Other than 0 means crash

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age cannot be 0.")
