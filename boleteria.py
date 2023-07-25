import random

animales = ['Ballena', 'Tigre', 'Anaconda', 'Panda', 'Tortuga']

def randomTicket():
    return [random.randint(0,1) for _ in range(2)]

def randomAnimal():
    return animales[random.randint(0,len(animales)-1)]

winnerTicket=randomTicket()
winnerAnimal=randomAnimal()
while True:
    ticketUser=randomTicket()
    boleto = input("Si logras adivinar el animal ganador, puedes volver intentar ganar otros premios con nuevo boleto ")
    print (f"Numero ganador es: {winnerTicket} y el animal ganador es:{winnerAnimal}, tu ticket es: {ticketUser}")
    if(winnerTicket==ticketUser and boleto == winnerAnimal):
        print("Ganaste")
        break
    else:
        print("Perdiste")




