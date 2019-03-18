course = "Python's course for Beginners"
print(course)

message = '''
Hi Piyush,

Here is an example of 3 quotes

So you see it is fun in "Python"

- From Omni
'''
print(message)

name = "Piyush"
print(name[0])  # First Index
print(name[-1])  # Index from end
print(name[0:3])  # Index Range(excludes last index e.g- 3 is excluded) Output: Piy
print(name[1:])  # All values from first index provided Output: iyush(since, first index was 1)
print(name[:])  # All values Output: Piyush

# Exercise
name = "Piyush"
print(name[1:-1])  # Outputs iyus(since it omits the last index when we use -ve index)

# Formatted String
first = "Piyush"
last = "Choubey"
msg = f'{first} [{last}] is a coder'
print(msg)  # Piyush Choubey is a coder

# Methods Here Course is "Python's course for Beginners"
wrong = 'piyush'

print(len(course))
print(course.upper())  # PYTHON'S COURSE FOR BEGINNERS
print(course.lower())  # python's course for beginners
print(course.find('P'))  # 0(Index Value)
print(course.find('10'))  # -1(Because there's no '10' in course)
print(course.find('Beginners'))  # 20(since, it gives the index where the B is)
print(course.replace('Beginners', 'Absolute Beginners'))  # Python's course for Absolute Beginners
print('Python' in course)  # True
print(wrong.title())  # Piyush
