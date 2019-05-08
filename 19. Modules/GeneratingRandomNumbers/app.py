# (Python module, in random — Generate pseudo-random numbers)
import random

for i in range(3):
    print(random.random())          # Generate pseudo-random numbers between 0-1


for i in range(3):
    print(random.randint(10, 20))   # Generate pseudo-random numbers between 10-20 (both inclusive)


members = ['Emily', 'Sara', 'Vasu', 'Natalie']
leader = random.choice(members)     # Chooses random item from list
print(leader)
