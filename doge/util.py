import cfg
def chat(sock,msg):
    sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHANN,msg).encode(encoding='utf_8', errors='strict'))
def serMsg(sock, set1, set2):
    sock.send("{} {}\r\n".format(set1, set2).encode(encoding='utf_8', errors='strict'))
    
def whisper(sock,name,msg):
    sock.send("PRIVMSG #{} :/w {} {}\r\n".format(cfg.CHANN,name,msg).encode(encoding='utf_8', errors='strict'))