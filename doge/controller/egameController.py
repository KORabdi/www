from model.egameModel import egameModel
#import dogegame
import util
import re
import time
from random import randint
from time import sleep
#from controller.pointsController import pointsController
 
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

class egameController:
    #Var
    points = object
    count = 0
    emotes = []
    emotesString = ""
    socket = object
    message = ""
    username = ""
    #constructor
    def __init__(self,socket):
        egame = egameModel()
        self.emotes = egame.get()
        self.emotesString = egame.getString()
        self.socket = socket
        #self.points = pointsController(socket)
    #method
    def start(self,name):
        if self.podminky(name) == False:
            util.chat(self.socket,"You dont have enough points to start game ConcernDoge")
            return
        util.chat(self.socket, "Guess emotes from: {}".format(self.emotesString))
        self.generate()
        self.get()

    def generate(self):
        self.count = randint(0,len(self.emotes))
        print(self.emotes[self.count])

    def get(self):
        previousMilis = 0
        while True:
            currentMillis = int(round(time.time() * 1000));
            response = self.socket.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                self.socket.send("PONG :tmi.twitch.tv\r\n".encode())
                print("PONG")
                continue
            self.username = re.search(r"\w+", response).group(0)
            self.message = CHAT_MSG.sub("",response)
            self.message = self.message.strip()
            
            if self.message not in self.emotes:
                continue
            
            if self.emotes[self.count] == self.message:
                util.chat(self.socket,"{} won 50 points PogChamp it was {}".format(self.username,self.message))
                #self.points.addAI(self.username, 50)
                return
            else:
                if currentMillis - previousMilis > 1000:
                    util.chat(self.socket,"{} not {}".format(self.username,self.message))
                    previousMilis = currentMillis

    def podminky(self, name):
#         if self.points.get(name) >= 100:
#             self.points.addAI(name,-100)
#             return True
        return True