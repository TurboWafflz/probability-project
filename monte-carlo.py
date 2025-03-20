# Find the time to contact a customer
# Returns (successfully contacted, time to contact)
def contact_customer():
    time = 0

    for i in range(4):
        result = call()
        time += result[1]

        if result[0]:
            return (True, time)

    return (False, time)

# Find the time a call attempt took
# Returns (successful call, time taken)
def call():
    time = 0
    
    # Dial call
    time += 6
    
    # Give up after 3 seconds if busy
    if busy:
        time += 3
        return (False, time)
    
    # Give up if not answered after 25 seconds
    if away_from_phone or time_to_answer >= 25:
        time += 25
        return (False, time)
   
    # Otherwise the call was successful
    time += time_to_answer
    return (True, time)


