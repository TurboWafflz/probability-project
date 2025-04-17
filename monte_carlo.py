import random
from math import log


# Find the time to contact a customer
# Returns (successfully contacted, time to contact)
def contact_customer():
    time = 0

    # Try to contact the customer 4 times, counting the time each call took
    for i in range(4):
        result = call()
        time += result[1]

        if result[0]:
            return (True, time)

    # If they didn't answer after four calls, give up
    return (False, time)


def expVar(mean):
    u_i = random.random()

    return -log(1 - u_i) / (1 / mean)


def bernVar(p):
    return random.random() < p


# Find the time a call attempt took
# Returns (successful call, time taken)
def call():
    time = 0

    # Dial call
    time += 6

    # Give up after 3 seconds if busy
    busy = bernVar(0.2)
    if busy:
        time += 3
        return (False, time)

    # Give up if not answered after 25 seconds
    away_from_phone = bernVar(0.3)
    time_to_answer = expVar(12)
    if away_from_phone or time_to_answer >= 25:
        time += 25
        return (False, time)

    # Otherwise the call was successful
    time += time_to_answer
    return (True, time)
