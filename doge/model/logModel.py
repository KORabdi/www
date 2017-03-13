from model.dibi import dibi
import re

class logModel:
    #Var 
    select = ""
    table = ""
    points = ""
    dibi = object
    data = {}
    #CONSTR
    def __init__(self,name,password,host,db):
        self.dibi = dibi(name,password,host,db)
    #meth
    def save(self,name,message):
        name = re.sub('[^A-Za-z0-9]+', '', name)
        self.dibi.query("INSERT INTO chat (name,message) VALUES ('{}','{}')".format(name,message))