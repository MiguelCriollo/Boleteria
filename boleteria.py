import random
def randomTicket():
    ticket=[]
    for num in range(4):
        ticket.append(random.randint(0,9))
    return ticket
print(randomTicket())