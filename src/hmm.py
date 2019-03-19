import random

for i in range(3):
    print(random.randint(10, 20))
    print(random.random())

members = ['Piyush', 'Anish', 'Iona']
leader = random.choice(members)
print(leader)

