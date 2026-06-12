# ibhwss idea(project),what we are building, how will we build, which concept we will use, pseudo code, streaching(adding advanced feature in it)

# //importing the random module 
import random

# create subjects
subjects = [
    "shahrukh khan",
    "virat kohli",
    "nirmala sitharaman",
    "a mumbai cat",
    "A group of monkey",
    "prime minister",
    "auto rickshaw driver from dehli",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]


place_things = [
    "at red fort",
    "in mumbai local train",
    "a plote of samosa",
    "at ganga ghat",
    "during ipl match",
    "aat india gate",
]


# start the headline generation 
while(True):
    subject= random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(place_things)

    headline = f"BREAKING NEWS {subject} {action} {place_thing}"
    print("\n"+headline)

    user_input = input("\nDo you want another headline (yes or no) : ").strip().lower()
    if user_input == "no":
        break

# print goodbye message as the terminating
print("\nthanks for using the fake news headline generator!!")
