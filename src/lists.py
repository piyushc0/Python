names = ['Phunt', 'Iona', 'Anish']
print(names[0])  # Phunt
print(names[-1])  # Anish
print(names[0:3])  # ['Phunt', 'Iona', 'Anish']
names[0] = 'Piyush'
print(names)  # ['Piyush', 'Iona', 'Anish']

numbers = [3, 6, 5, 8, 9, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

