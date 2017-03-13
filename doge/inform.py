import cfg
import util

class inform:
    #Var
    data = ""#data from txt file
    socket = object
    
    #constr
    def __init__(self,socket):
        print ("inform module is on...")
        self.socket = socket
    
    #meth
    def start(self,message):
        self.getData()
        self.createJson()
        json = self.getJson()#import json file
        #find !<COMMAND> in message and get data from json if no command return code 404
        
    
    def getData(self):
        #TODO: file system
        #open file cfg.INFORMFILE
        self.data = "" #getdata
        #close file
        
    def createJson(self):
        print("TODO: create JSON file")
    
    def getJson(self):
        print("Import JSON file")
    