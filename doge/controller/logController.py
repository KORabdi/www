from model.logModel import logModel
import cfg

class logController:
    def __init__(self,socket):
        self.socket = socket
        self.database = logModel(cfg.DBNAME,cfg.DBPASS,cfg.DBHOST,cfg.DB)
    
    def log(self,name,message):
        self.database.save(name,message)