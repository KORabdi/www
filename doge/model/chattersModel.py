from model import requests

class chattersModel:
    #Var
    
    #constructor
    def __init__(self):
        print()
    #methods
    def get(self):
        r = requests.get("http://tmi.twitch.tv/group/user/shaflumbles/chatters")
        r.encoding
        jsonr = r.json()
        return jsonr['chatters']['viewers']+jsonr['chatters']['moderators']