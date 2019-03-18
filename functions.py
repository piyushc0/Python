def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


greet_user('Piyush', 'Choubey')  # Positional Argument

# Better Functions
# Param - Placeholder
# Argument -  Values in place of param

# Keyword Argument
greet_user(last_name="Choubey", first_name="Piyush")


# Square
def square(x):
    return x ** 2


print(square(24))

