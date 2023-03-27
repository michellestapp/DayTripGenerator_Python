# Day Trip Generator in Python

# Main Stories


# (5 points): As a developer, I want to make at least three commits with descriptive messages 
# DONE (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and 
#              entertainment in their own separate Lists. 
# DONE (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# DONE (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# DONE (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# DONE (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# DONE (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of 
#             transportation, and/or form of entertainment if I don’t like one or more of those things.
# DONE (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of 
#             the random selections.
# (10  points): As a user, I want to display my completed trip in the console
# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. 
#             Remember, each function should do just one thing! 


destinations = ['Puerto Vallarta', 'Chicago', 'Albuquerque', 'New york City', 'Orlando']
restaurants = ['Cracker Barrel', 'Olive Garden', 'IHOP', 'Golden Corral', 'Mi Lupita', 'Los Cuates', 'The Frontier']
transportations = ['air','car','carriage','bus', 'limo', 'walking']
entertainments = ['movie','bar','aquarium','amusment park', 'pool','luau']
options = [destinations, transportations, restaurants, entertainments]



import random


def print_current_choices(options):
    print(f"\n  Your amazing day trip will go to {options[0]} by {options[1]}. \n  You will eat at {options[2]} and then go to the {options[3]}.\n")

happy_with_choices = 'n'

def select_options():
    destination = random.choice(destinations)
    transportation = random.choice(transportations)
    restaurant = random.choice(restaurants)
    entertainment = random.choice(entertainments)
    return [destination,transportation, restaurant, entertainment]



daytrip = select_options()


while happy_with_choices == 'n':
    print_current_choices(daytrip)

    happy_with_choices = input(f"\n  Are you happy with the trip that has been created for you? Press 'y' if you are or 'n' if not:  ")

    if happy_with_choices == 'y':
        break

    else:
        choice_number = input(f" Which would you like to change? \n Press 1 for destination \n Press 2 for transportation \n Press 3 for restaurant \n Press 4 for entertainment: ")
        index = int(choice_number) - 1
        daytrip[index] = random.choice(options[index])

        # if choice_number == '1':
        #     destination = random.choice(destinations)
        
 
        # elif choice_number == '2':
        #     transportation = random.choice(transportations)
       
       
        # elif choice_number == '3':
        #     restaurant = random.choice(restaurants)
        
       
        # elif choice_number == '4':
        #     entertainment = random.choice(entertainments)
       
      
        # else:
        #     print(" I did not understand your input.")
    

 
    

print(f"\n   HAVE A GREAT TRIP!!!  \n")
        
    





