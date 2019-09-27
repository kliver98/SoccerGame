from _thread import *

class Room():
    
    def __init__(self,iden):
        self.id=iden
        self.avaible=True
        self.p1_pos=(100,100)
        self.p2_pos=(800,600)
        self.p1=None
        self.p2=None
        self.ball=(448,251)
    
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
        self.send_info(net, pos, self.ball)
        #net.send(str.encode(self.make_pos(pos)))
        reply = ""
        while True:
            try:
                #data = self.read_pos(net.recv(2048).decode())
                data=self.read_info(net)
                #pos = data

                if not data:
                    print("Disconnected")
                else:
                    player_pos=(data[0],data[1])
                    if player == self.p1:
                        self.p1_pos=player_pos
                        reply = self.p2_pos
                    elif player== self.p2:
                        self.p2_pos=player_pos
                        reply = self.p1_pos
                    
                    #print("Received: ", data)
                    #print("Sending : ", reply)

                #net.sendall(str.encode(self.make_pos(reply)))
                
                self.send_info(net, reply,self.ball)
                self.ball=(data[2],data[3])
            except Exception as e:
                print(e.trace_call())
                break

        print("Lost connection")
        net.close()
    
    def send_info(self,net,reply,ball):
        net.sendall(str.encode(f"{reply[0]},{reply[1]},{ball[0]},{ball[1]}"))
    
    def read_info(self,net):
        str=net.recv(2048).decode().split(',')
        if str is not None:
            return str
        else:
            (1,1,500,500)
    def ball_pos(self): 
        return f"ball,{self.ball[0]},{self.ball[1]}"
    
    def is_avaible(self):
        return self.avaible
    
    def read_pos(self,str):
        str = str.split(",")
        try:
            return int(str[0]), int(str[1])
        except:
            return 100,100
    def read_ball(self,data):
        ball_info=data.split(',')
        self.ball[0]=ball_info[1]
        self.ball[1]=ball_info[1]
        
    def make_pos(self,tup):
        return str(tup[0]) + "," + str(tup[1])
    
    def check_avaible(self):
        if self.p1 is None:
            self.avaible=True
        elif self.p2 is None:
            self.avaible=True
        else:
            self.avaible=False