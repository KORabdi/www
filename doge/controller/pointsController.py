import cfg  
import util
from model.pointsModel import pointsModel  
import string
from controller.chattersPresenter import chattersPresenter   

class pointsController: 
    #Var
    database = object
    socket = object
    chatters = object
    #construactor
    def __init__(self,socket):
        self.socket = socket
        self.database = pointsModel(cfg.DBNAME,cfg.DBPASS,cfg.DBHOST,cfg.DB)
        self.database.load(0)
        self.chatters = chattersPresenter()
    #meth
    def add(self,name,message): #adding points in chat way
        if self.checkPermission(name) == False:
            util.chat(self.socket, "PERMISSION DENIED ConcernDoge")
            return
        try:
            arr = message.split(' ') #arr[0] - command, #arr[1] - name, #arr[2] - amount
            print(arr[1])
            arr[1] = arr[1].replace("\r\n","").lower()
            points = self.database.getPoints(arr[1])
            self.database.setPoints(arr[1],str(points+int(arr[2])))
            util.whisper(self.socket, "{} SUCCESS ConcernDoge".format(name))
        except:
            util.whisper(self.socket, "{} ERROR ConcernDoge".format(name))

    def addAI(self,name,pointsToAdd): #adding points in programme way
        points = self.database.getPoints(name)
        self.database.setPoints(name,str(points+pointsToAdd))
    
    def addall(self,pointsToAdd):
        chatters = self.chatters.get()#get active user (create model (list) of active users)
        for name in chatters:
            self.userExists(name)
            self.addAI(name,pointsToAdd)

    def show(self,name):
        name = name.replace("\r\n","").lower()
        points = self.database.getPoints(name)
        strVar = "{}, you have {} doge points ConcernDoge".format(name,points)
        util.chat(self.socket, strVar)
    
    def get(self,name):
        points = self.database.getPoints(name)
        return points
    
    def checkPermission(self,name):
        for x in cfg.ADMINLIST:
            if name == x:
                return True
        return False

    def userExists(self,name):
        if self.database.isUserExists(name) == False:
            self.database.createUser(name)