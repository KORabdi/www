HOST = "irc.twitch.tv"
PORT = 6667
NICK = "4Head_4Head___"
PASS = "oauth:grckabmji1g2etzxkk6r4qeftq23gk"
CHANN = "zetalot"
BOT = "ShibaDogeBot"
MASTER = "korandi"
INTERVAL = 1.1 #IN SECONDS
MGGINTERVAL = 2
INFORMFILE = "inform.txt"
DBNAME="root"
DBPASS=""
DBHOST="127.0.0.1"
DB="semestralka"
ADMINLIST = ["korandi","shaflumbles","ShibaDogeBot"]

class cfgBot():
    NICK = "4Head_4Head___"
    PASS = "oauth:grckabmji1g2etzxkk6r4qeftq23gk"
    
    def __init__(self):
        print ("Bot settings is on...")
        
    def setBot(self,x):
        if(x == '1'):
            self.NICK = "4Head_4Head_"
            self.PASS = "oauth:5cphc8yw0574a1heg0tstefgnq0z1i"
        elif(x == 'kor'):
            self.NICK = "Korandi"
            self.PASS = "oauth:m9p6nz230cbbpds7ugpseonqmkpyue"            
        elif(x == 'sb'):
            self.NICK = "ShibaDogeBot"
            self.PASS = "oauth:cpsgqmwbu1blikdpcef22e87fgc1fx"
        elif(x == '2'):
            self.NICK = "4Head_4Head__"
            self.PASS = "oauth:631rik9jaqvp3ggguey76vqxarynhy"
        else:
            self.NICK = "4Head_4Head___ "
            self.PASS = "oauth:z3soc2h60bvcfn2wh6dnk7jo1s0ivt"