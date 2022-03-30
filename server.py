import socket
import sys
import random
import time

if len(sys.argv) != 2:
    print("Correct usage: script, port number")
    exit()


Ip = "127.0.0.1"
Port = int(sys.argv[1])

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((Ip, Port))
serverSocket.listen()

connected = []
clients = []
print("===========================  WELCOME TO CHAAAATROOM  ===========================")

t = time.localtime()
current_time = time.strftime("%H:%M", t)

while True:
    print('Waiting for connections...')
    clientSocket, clientAddress = serverSocket.accept()
    connected.append(clientSocket)

    bot = clientSocket.recv(1024).decode()
    clients.append(bot)
    print(bot, "joined the chat")

    message = input("Do you want to add more users, type yes or no?"+ "\n"+current_time+", Server:")
    if message == 'no':
        break



while True:
    # The chat the bots are going to answear back to
    # It takes input from the user, but if you whould like the server to chose for you
    # action = random.choice(["drink", "clean", "eat", "sleep", "study", "think", "work", "party"])
    # host_msg = "Host: Do you guys want to {} today? ".format(action)
    print('What do you want to do?')
    hostMsg = input(current_time + ', Server: ')
    print("Server: " + hostMsg)


#Remove peopel from the list after quit
    if hostMsg == 'quit':

        for c in connected:
            bot_index = connected.index(c)
            bot_name = clients[bot_index]
            c.close()
            print(bot_name, "has disconected")
            connected.remove(c)
            clients.remove(bot_name)
        break


    # Sendt the messages thorugh the clients
    for i in connected:
        i.send(hostMsg.encode())
    for i in connected:
        message = i.recv(1024).decode()
        print(message)
        for j in connected:
            if j != i:
                j.send(b"Bot:" + message.encode())
