from model.mysql.mysql.connector import connect
class dibi():
    #var
    tableVar = ""
    selectVar = ""
    setVar=""
    whereVar = []
    methodVar = ""
    cnx = object
    TABLES = {}
    #constr connect to database
    def __init__(self,user,password,host,database):
        self.cnx = connect(user=user, password=password,
                              host=host,
                              database=database)
        #self.cnx.close()
    #methods
    def method(self,method):
        self.methodVar = method
        return self
    
    def select(self,select):
        self.selectVar = select
        return self
    
    def where(self,where):
        self.whereVar = where
        return self
    
    def table (self,table):
        self.tableVar = table
        return self
    
    def set(self,set):
        self.setVar = set
        return self
    
    def update(self):
        #todo check if column, table, exists if not, create!
        query = "UPDATE "+self.tableVar+" SET "+self.setVar+" WHERE "+self.whereVar
        cursor = self.cnx.cursor()
        cursor.execute(query)
        self.cnx.commit()
        cursor.close()
        #self.cnx.close()        
    
    def fetchAll(self):
        #todo check if column, table, exists if not, create!
        if self.whereVar == "1=1":
            query = "SELECT "+self.selectVar+" FROM `"+self.tableVar+"`"
        else:
            query = "SELECT "+self.selectVar+" FROM `"+self.tableVar+"` WHERE "+self.whereVar+""
        cursor = self.cnx.cursor()
        cursor.execute(query)
        #self.cnx.commit()
        toReturn = cursor.fetchall()
        cursor.close()
        #self.cnx.close()
        return toReturn
    
    def fetchOne(self):
        if self.whereVar == "1=1":
            query = "SELECT "+self.selectVar+" FROM `"+self.tableVar+"`"
        else:
            query = "SELECT "+self.selectVar+" FROM `"+self.tableVar+"` WHERE "+self.whereVar+""
        cursor = self.cnx.cursor()
        cursor.execute(query)
        #self.cnx.commit()
        toReturn = cursor.fetchone()
        cursor.close()
        #self.cnx.close()
        return toReturn
    
    def query(self,query):
        cursor = self.cnx.cursor()
        cursor.execute(query)
        self.cnx.commit()
        #toReturn = cursor.fetchall()
        cursor.close()
        #return toReturn