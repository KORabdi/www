from config.emotelist import EMOTES
 

class egameModel:
    #Var
    emotes = ""
    #constructor
    def __init__(self):
        self.emotes = EMOTES
    #methody
    def get(self):
        return self.emotes
    
    def getString(self):
        y = ""
        for x in self.emotes:
            y= y+" "+x
        return y