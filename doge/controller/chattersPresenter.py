from model.chattersModel import chattersModel

class chattersPresenter: 
    #Var
    database = object
    #constructor
    def __init__(self):
        self.database = chattersModel()
    #methods
    def get(self):
        return self.database.get()