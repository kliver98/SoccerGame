'''
Created on 22/09/2019

@author: JORGE
'''
import socket
##from _thread import *
import sys
from server import room

server = input("Please insert the ip server, it will be locallhost for defect")
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    if server is None:
        server="localhost"
    
    
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(6)
print("server was started, waiting for connections")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]

'''def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
               
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except Exception as e:
            print(e.trace_call())
            break

    print("Lost connection")
    conn.close()'''

#return the room that are aviable , None if 
def verified_aviabled():
    r=None
    for i in roomList:
        if i.is_avaible():
            return i
    return r

currentPlayer = 0
currentRoom=0
roomList=[]

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    r= verified_aviabled()
    if r is None:
        r=room.Room(currentRoom)
        roomList.append(r)
        currentRoom+=1
    #start_new_thread(threaded_client, (conn, currentPlayer))
    r.add_player(conn, currentPlayer)
    currentPlayer += 1