import cfg
import util
import time
import socket 
import re 
from util import serMsg
from time import sleep
import dogegame
from controller.logController import logController
#from controller.pointsController import pointsController
from controller.egameController import egameController

x = input('# of bot:')
y = cfg.cfgBot()
y.setBot(x)

s = socket.socket()
s.connect((cfg.HOST,cfg.PORT))

serMsg(s, "PASS",y.PASS)
serMsg(s, "NICK", y.NICK)
serMsg(s, "JOIN", "#"+cfg.CHANN)

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

varDoge = dogegame.doge(s)
log = logController(s)

#points = pointsController(s)

egame = egameController(s)

#util.chat(s, "ConcernDoge /")
print("ok")

previousMilis = 0

#def addPointsAll():
#    print ("points added")
#    xpreviousMilis = currentMillis
#    points.addall(2)
#    return xpreviousMilis
while True:
    try:
        currentMillis = int(round(time.time() * 1000));
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode())
            print("PONG")
            continue
        username = re.search(r"\w+", response).group(0)
        message = CHAT_MSG.sub("",response)
        #print(username)
#         log.log(username, message)
        if "!kstart\r\n" == message and username in ['korandi','fubid','igetnokick','zetalot']:
            varDoge.start(username)
        if "!estart\r\n" == message and username in ['korandi','fubid','igetnokick','zetalot']:
            egame.start(username)
    except:
        pass
    
    
    
    #points.userExists(username)

    #if currentMillis - previousMilis > 60000:
    #    previousMilis = addPointsAll()

    #if "!dogegame\r\n" == message and username != 'Nightbot':
    #    if currentMillis - previousMilis > 60000:
    #        previousMilis = currentMillis
    #        varDoge.start(username)
    #    else:
    #        util.chat(s,'It is too early, just wait a bit FeelsBadMan ')
        
#    if "!egame\r\n" == message and username != 'Nightbot':
#        egame.start(username)

#    if "!addpoints" in message:
#        points.add(username,message)

#   if "!points" in message:
#       arr = message.split(' ')
#       try:
#           arr[1]
#           points.show(arr[1])
#       except:
#           points.show(username)
