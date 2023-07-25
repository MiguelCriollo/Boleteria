boleto = input("Si logras adivinar el animal ganador, puedes volver intentar ganar otros premios con nuevo boleto ")
animales = ['Ballena', 'Tigre', 'Anaconda', 'Panda', 'Tortuga']
resultado = ['Perdedor', 'Perdedor', 'Ganador', 'Perdedor', 'Ganador']

if boleto in [animales[i] for i in range(len(animales)) if resultado[i] == 'Ganador']:
    print("Felicitaciones, has adivinado correctamente y obtienes otro boleto!")
else:
    print("Lo siento, no has adivinado correctamente.")