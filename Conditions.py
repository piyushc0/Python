# If Else

is_Hot = True
is_Cold = False

if is_Hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_Cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Exercise
price = 1000000
has_good_credit = True
has_high_income = False
has_criminal_record = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")

# Logical AND operator
if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Not Eligible")

# Logical OR operator
if has_good_credit or has_high_income:
    print("Eligible for loan")
else:
    print("Not Eligible")

# Logical AND NOT operator
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible")

# Comparison Operator
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a not day")

# Other operators
print(temperature == 30)  # True
print(temperature < 30)  # False
print(temperature <= 30)  # True
print(temperature >= 30)  # True
print(temperature != 30)  # False

# Weight Converter
weight = input('Weight: ')
unit = input('What is your input in (l)bs or (k)g: ')
if unit.lower() == 'l':
    converted = int(weight) * 0.45
    print(f"Your weight is {converted} kg")
elif unit.lower() == 'k':
    converted = int(weight) / 0.45
    print(f"Your weight is {converted} lbs")
else:
    print("Valid units are (l)bs or (k)g")
