import random
import datetime

post = []


def getKeywords():
    """ Random temperature calculation """
    temp = str(random.randint(-30, 30))
    if temp == 1 or temp == -1:
        temp += " degree"
    temp += " degrees"

    """ Random time calculation """
    hour = str(random.randint(0, 23))
    minutes_tens = str(random.randint(0, 5))
    minutes_ones = str(random.randint(0, 9))
    time = str(hour + ":" + minutes_tens + "" + minutes_ones)

    """ Random estimated time or arrival calculation """
    eta = str(str(random.randint(5, 60)) + " minutes")

    """ Random date calculation """
    start = datetime.date(2022, 1, 1)
    end = datetime.date(2022, 12, 31)
    rand_range = end - start
    days_between_dates = rand_range.days
    rand_range = random.randrange(days_between_dates)
    day = str(start + datetime.timedelta(days=rand_range))

    """ Random holiday calculation """
    holiday = ["Christmas", "Thanksgiving", "Easter", "Halloween", "Labour day"]
    holi = (random.choice(holiday))

    """ Random location calculation """
    location = ["work", "home", "the office", "the store", "the gas station"]
    loc = (random.choice(location))

    """ Random relative time calculation """
    relativeTime = ["today", "tomorrow", "next week", "next month"]
    relative = (random.choice(relativeTime))

    """ Random relative time calculation """
    number = str(random.randint(2, 10))

    keywords = [temp, time, eta, day, holi, loc, relative, number]
    return keywords


def generatePost():
    x = random.randint(1, 14)
    n = 0

    keywords = getKeywords()
    temp = keywords[0]
    time = keywords[1]
    eta = keywords[2]
    day = keywords[3]
    holi = keywords[4]
    loc = keywords[5]
    relative = keywords[6]
    number = keywords[7]

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
    elif x == 10:
        n = "I’m leaving for my break at " + time + "."
    elif x == 11:
        n = "I am working from home on " + day + "."
    elif x == 12:
        n = "I am working from the office on " + day + "."
    elif x == 13:
        n = "There’s construction on the highway heading to " + loc + "."
    elif x == 14:
        n = "There are " + number + " people in my office today."
    else:
        print("Unknown sentence structure")
    print(n)
    post.append(n)


for i in range(100):
    generatePost()

print(post)
