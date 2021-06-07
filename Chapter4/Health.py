##project 1
import random

#Giving a player health
health = 50

#Creating a difficulty setting
difficulty = 1 

#creating a health potion generating a random amount of health 
# Converting a float to an interger using the int() function
health_potion = int(random.randint(25,50) / difficulty)

# Adding a potion to the current health
health += health_potion
# health = health + health_potion

print(health)
 