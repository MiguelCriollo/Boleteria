import random
def randomTicket():
    return [random.randint(0,) for _ in range(4) ]


while True:
    winnerTicket=randomTicket()
    input("Enter para comprar ticket")
    ticketUser=randomTicket()
    print (f"Numero ganador es: {winnerTicket}, tu ticket es: {ticketUser}")
    if(winnerTicket==ticketUser):
        print("Ganaste")
        break
    else:
        print("Perdiste")

