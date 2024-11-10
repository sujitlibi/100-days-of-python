# Figure out how to pick a random name from the list of friends.
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_number = random.randint(0, len(friends) - 1)

print(f"{friends[random_number]} will pay the bill today!!!!!!")

# Method 2:
# print(f"{random.choice(friends) will pay the bill today!!!!!!}") ===> one line code hehehe