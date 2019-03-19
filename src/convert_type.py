# Basic Operation

name = input('What is your name? ')
print(type(name))
color = input('What Color do you like? ')
age = input('What is your Age? ')
year = 2019 - int(age)
print(type(year))

print(f'{name} was born in {year}')

# Weight Converter
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Other Type conversion
int()
bool()
str()
float()
chr(10)
