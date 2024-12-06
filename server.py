
import socket
from _thread import *
from functions import Game
from classes import Player
import pickle
import functions
import classes
import screens
import sys

server = "192.168.1.217"
port = 5557
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    print('successful')
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
idCount = 0
games = {}


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(pickle.dumps(p))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048*2))
            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data[0] == "add player":
                        games[gameId].gameplayers = data[1]
                    elif data[0] == "dealing cards":
                        games[gameId].dealtCards = data[1]
                        games[gameId].openCards = data[2]
                        games[gameId].correctGuess.weapon = data[3].weapon
                        games[gameId].correctGuess.character = data[3].character
                        games[gameId].correctGuess.room = data[3].room
                        games[gameId].gameplayers = data[4]
                    elif data[0] == "verify cards":
                        conn.sendall(pickle.dumps(game))
                    elif data[0] == "end turn":
                        games[gameId].gameplayers = data[1]
                    elif data[0] == "add players":
                        games[gameId].gameplayers = data[1]
                    elif data[0] == "move player":
                        games[gameId].gameplayers[data[1]].x = data[2].x
                        games[gameId].gameplayers[data[1]].y = data[2].y
                    elif data[0] == "verify screen":
                        conn.sendall(pickle.dumps(game))
                    elif data[0] == "suggestion":
                        games[gameId].globalprompt = data[1]
                    elif data[0] == "accusation":
                        games[gameId].globalprompt = data[1]
                    elif data[0] == "update prompt":
                        games[gameId].globalprompt = data[1]
                    elif data[0] == "update screen":
                        conn.sendall(pickle.dumps(game))
                    conn.sendall(pickle.dumps(game))

            else:
                break
        except:
            break
    print("Lost connection")
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    p = idCount
    idCount += 1

    gameId = 1
    if idCount < 3:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
    start_new_thread(threaded_client, (conn, p, gameId))
