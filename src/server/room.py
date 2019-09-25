from _thread import *

class Room():
    
    def __init__(self,iden):
        self.id=iden
        self.avaible=True
        self.p1_pos=(100,100)
        self.p2_pos=(800,600)
        self.p1=None
        self.p2=None
    
    
    def add_player(self,net,playerid):
        if self.p1 is None:
            self.p1=playerid
        elif self.p2 is None:
            self.p2=playerid
            
        start_new_thread(self.threaded_client, (net, playerid))
        self.check_avaible()
        
    def threaded_client(self,net, player):
        pos=None
        if player==self.p1:
            pos=self.p1_pos
        elif player==self.p2:
            pos=self.p2_pos    
        
        net.send(str.encode(self.make_pos(pos)))
        reply = ""
        while True:
            try:
                data = self.read_pos(net.recv(2048).decode())
                #pos = data

                if not data:
                    print("Disconnected")
               
                else:
                    if player == self.p1:
                        self.p1_pos=data
                        reply = self.p2_pos
                    elif player== self.p2:
                        self.p2_pos=data
                        reply = self.p1_pos

                    #print("Received: ", data)
                    #print("Sending : ", reply)

                net.sendall(str.encode(self.make_pos(reply)))
            except Exception as e:
                print(e.trace_call())
                break

        print("Lost connection")
        net.close()
    
    
    def is_avaible(self):
        return self.avaible
    
    def read_pos(self,str):
        str = str.split(",")
        return int(str[0]), int(str[1])
    
    def make_pos(self,tup):
        return str(tup[0]) + "," + str(tup[1])
    
    def check_avaible(self):
        if self.p1 is None:
            self.avaible=True
        elif self.p2 is None:
            self.avaible=True
        else:
            self.avaible=False