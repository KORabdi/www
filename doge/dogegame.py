import util
import re
import time
from random import randint
from collections import Counter
from time import sleep
from controller.pointsController import pointsController
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")


class doge:
    #Var
    count = 0
    socket = object
    username = ""
    message = ""
    points = object
    #konstruktor
    def __init__(self,socket):
        print("ready to spam")
        self.socket = socket
        #self.points = pointsController(self.socket)
    #metody
    def start(self,name):
        if self.podminky(name) == False:
            util.chat(self.socket,"You dont have enough points to start game ConcernDoge")
            return
        util.chat(self.socket, "Guess number of Kappa from 1-25")
        self.generate()
        self.get()
    def generate(self):
        self.count = randint(1,10)
        print(self.count)
    def get(self):
        previousMilis = 0
        while 1==1:
            currentMillis = int(round(time.time() * 1000));
            response = self.socket.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                self.socket.send("PONG :tmi.twitch.tv\r\n".encode())
                print("PONG")
                continue
            self.username = re.search(r"\w+", response).group(0)
            self.message = CHAT_MSG.sub("",response)
            self.message = self.message.strip()
            words = self.message.split()
            wordCount = Counter(words)
            
            if "!kill" in self.message and self.username == "korandi":
                print (self.username)
                util.chat(self.socket,"RIP. FeelsBadMan")
                return
            
            if "Kappa" not in self.message:
                continue
            
            if "Kappa" in self.message:
                if self.username == "korandi":
                    continue
                if wordCount['Kappa'] == self.count:
                    #self.points.userExists(self.username)
                    util.chat(self.socket, "{} won 50 points! PogChamp".format(self.username))
                    #self.points.addAI(self.username,50)
                    return True
                else:
                    if currentMillis - previousMilis > 1000:
                        util.chat(self.socket, "{} nope! Kappa".format(self.username))
                        previousMilis = currentMillis
        
    def podminky(self,name):
        #if self.points.get(name) >= 100:
        #    self.points.addAI(name,-100)
        #    return True
        #return False
        return True