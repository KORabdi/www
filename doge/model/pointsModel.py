from model.dibi import dibi


class pointsModel:
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
    def load(self,id):
        if id == 0:
            self.where = "1=1"
        else:
            self.where = "id="+id
        self.table = "points"
        self.select = "*"
        
        data = self.dibi.select(self.select).table(self.table).where(self.where).fetchAll()
        self.setData(data)
    
    def setData(self,data):
        datax = {}
        for x in data:
            datax["id"] = x[0]
            datax["points"] = x[2]
            self.data[x[1].decode("utf-8")] = datax
    
    def getData(self):
        return self.data
    
    def getId(self,name):
        return self.data[name]['id']
    
    def getPoints(self,name):
        try:
            data = self.dibi.select(self.select).table(self.table).where("Name='"+name+"'").fetchOne()
            data[2]
        except:
            return 0
        return data[2]
    
    def setPoints(self,name,points):
        self.dibi.table(self.table).where("Name='"+name+"'").set("Points='"+points+"'").update()
        
    def isUserExists(self,name):
        data = self.dibi.select(self.select).table(self.table).where("Name='"+name+"'").fetchOne()
        try:
            data[3]
            return True
        except:
            return False

    def createUser(self,name):
        self.dibi.query("INSERT INTO points (Name,Points) VALUES ('"+name+"',100)")