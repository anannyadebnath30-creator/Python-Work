# Q4.2 random library demonstration
import random
print("Random integer (1-100):", random.randint(1, 100))
items = ["Python", "Java", "SQL", "HTML"]
print("Original list:", items)
print("Random choice:", random.choice(items))
random.shuffle(items)
print("Shuffled list:", items)
