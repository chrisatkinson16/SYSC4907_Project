import random

post = []

temperature = ["21 degrees", "30 degrees", "-5 degrees", "-15 degrees", "-30 degrees"]
location = ["work", "home", "the office", "the store", "the gas station"]
currentTime = ["8 AM", "5 PM", "10 AM", "3 PM", "12 AM"]
ETA = ["5 minutes", "10 minutes", "15 minutes", "20 minutes", "25 minutes"]
holiday = ["Christmas", "Thanksgiving", "Easter", "Halloween", "Labour day"]
date = ["November 20th 2021", "January 1st 2022", "March 12th 2022", "April 29th 2022", "October 23th 2022"]
inOut = ["inside", "outside"]
relativeTime = ["today", "tomorrow", "next week", "next month"]


def formSentence():
    x = random.randint(1, 9)

    temp = (random.choice(temperature))
    loc = (random.choice(location))
    time = (random.choice(currentTime))
    eta = (random.choice(ETA))
    holi = (random.choice(holiday))
    day = (random.choice(date))
    relative = (random.choice(relativeTime))

    if x == 1:
        n = "It is " + temp + " outside right now."
    elif x == 2:
        n = "It is " + temp + " at " + loc + " right now."
    elif x == 3:
        n = "I am arriving at " + loc + " in " + eta + "."
    elif x == 4:
        n = "I am arriving at " + loc + " at " + time + "."
    elif x == 5:
        n = "The office will be closed on " + day + "."
    elif x == 6:
        n = "Because of " + holi + ", we will be closed for the day."
    elif x == 7:
        n = "Because of " + holi + ", we will close at 1 PM for the day."
    elif x == 8:
        n = "I won't make it to work until " + time + " " + relative + "."
    elif x == 9:
        n = "I am going to be " + eta + " late to work today."
    else:
        print("Unknown sentence structure")
    print(n)
    post.append(n)


for i in range(10):
    formSentence()


print(post)
