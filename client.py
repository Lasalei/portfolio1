
import random
import socket
import sys

Ip = str(sys.argv[1])
Port = int(sys.argv[2])
Bot = str(sys.argv[3])




clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((Ip, Port))

print("You successfully joined the chat 😁")
clientSocket.send(Bot.encode())


good_Things = ["Party", "drink", "scream", "eat", "catch", "sing", "sleep", "think"]
bad_Things = ["cry", "steal", "beat", "clean", "study", "work"]
randomAction = random.choice(["die", "paint a wall green", "wash our clothes", "kick a ball", "buy some popcorn"])

def las(a):
    if a in bad_Things:
        return "Las: I dont think {} is such a great idea... Cant we do anything else such as {}?".format(a + "ing", random.choice(good_Things))
    else:
        return "Las: I think {} sounds great!".format(a + "ing")
def aws(a, b = None):
    if a in bad_Things:
        return "Aws: Omg, {} is the beeeeest!".format(a + "ing")
    else:
        return "Aws: Omg, {} its lame, lets go {} instead".format(a + "ing", b)
def bob(a, b):
    return "Bob: I will rather {} than {}, but whatever...".format(b,a)
def ricardo(a):
    return "Ricardo: I dont appreciate {}.".format(a + "ing")


while True:
    hostMsg = clientSocket.recv(1024).decode('ascii')
    if "Bot:" in hostMsg:
        print(hostMsg[4:])
        continue
    else:
        print(hostMsg)

    print(hostMsg)

    try:
        splitMsg = hostMsg.split()
        action = splitMsg[3]
    except:
        exit()

    randomAction = random.choice(["work", "run a martoon", "iron my clothes", "through a ball"])

    if Bot == 'Las':
        message = "{}".format(las(action))
    elif Bot == 'Aws':
        message = "{}".format(aws(action, randomAction))
    elif Bot == 'Bob':
        message = "{}".format((bob(action, randomAction)))
    elif Bot == 'Ricardo':
        message = "{}".format(ricardo(action))
    else:
        message = "Server: {} isnt availabe ".format(Bot)

    clientSocket.send(message.encode())
    print(message)



