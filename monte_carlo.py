import random
from math import floor, log
from statistics import median


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
        # Hang up time
        time += 1
        return (False, time)

    # Otherwise the call was successful
    time += time_to_answer
    return (True, time)


def main():
    NUM_CALLS = 1000

    customers = [contact_customer() for i in range(NUM_CALLS)]
    total_time = sum([customer[1] for customer in customers])
    customers_called = len([customer for customer in customers if customer[0]])

    print(f"Customers reached: {customers_called}")
    print(f"Time taken: {total_time} seconds")
    print(f"Mean time per customer: {total_time / customers_called} seconds")
    print(
        f"Median time per customer: {median([customer[1] for customer in customers])}"
    )

    print(f"First quartile: {customers[floor(NUM_CALLS * 0.25)][1]}")
    print(f"Third quartile: {customers[floor(NUM_CALLS * 0.75)][1]}")

    w_le_15 = len([customer for customer in customers if customer[1] <= 15]) / NUM_CALLS
    w_le_20 = len([customer for customer in customers if customer[1] <= 20]) / NUM_CALLS
    w_le_30 = len([customer for customer in customers if customer[1] <= 30]) / NUM_CALLS
    w_g_40 = len([customer for customer in customers if customer[1] > 40]) / NUM_CALLS

    print(f"P[W <= 15]: {w_le_15}")
    print(f"P[W <= 20]: {w_le_20}")
    print(f"P[W <= 30]: {w_le_30}")
    print(f"P[W > 40]: {w_g_40}")

    W = [75, 100, 125]

    for w in W:
        P = len([customer for customer in customers if customer[1] > w]) / NUM_CALLS
        print(f"P[W > {w}]: {P}")


if __name__ == "__main__":
    main()
