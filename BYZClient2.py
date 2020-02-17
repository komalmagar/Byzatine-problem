import socket
import pickle
import time
ss1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "127.0.0.1"
port = 9993
ss1.bind((ip, port))

msg1 = input("please enter value for client1:")
port1 = 9991
ss1.sendto(msg1.encode().strip(), (ip, port1))

msg2 = input("please enter value for client2:")
port2 = 9992
ss1.sendto(msg2.encode().strip(), (ip, port2))

msg4 = input("please enter value for client4:")
port4 = 9994
ss1.sendto(msg4.encode().strip(), (ip, port4))

c = 0
StoreInfo = [0,0,0,0]
while True:
    data, changer = ss1.recvfrom(1024)
    v = data.decode()
    if data:
        c = c + 1
        print("recv from", changer)
        if changer[1] == 9991:
            StoreInfo[0] = v
        if changer[1] == 9992:
            StoreInfo[1] = v
        if changer[1] == 9994:
            StoreInfo[3] = v
    if c == 3:
        break
print("my array:", StoreInfo)

time.sleep(5)
sdata = pickle.dumps(StoreInfo)
ss1.sendto(sdata, (ip, port1))
ss1.sendto(sdata, (ip, port2))
ss1.sendto(sdata, (ip, port4))

v1=v2=v4=[]
c=0
while True:
    data, changer = ss1.recvfrom(1024)
    v=pickle.loads(data)
    if data:
        c = c + 1
        print("recv from ", changer)
        if changer[1] == 9991:
            v1 = v
        if changer[1] == 9992:
            v2 = v
        if changer[1] == 9994:
            v4 = v

    if c == 3:
        break

print("all arrays ",v1," ", v2, " ",v4)

if StoreInfo[0]==v2[0]==v4[0]:
    print("client 1 is innocent")
else:
    print("client 1 is not innocent")

if StoreInfo[1]==v1[1]==v4[1]:
    print("client 2 is innocent")
else:
    print("client 2 is not innocent")

if StoreInfo[3]==v1[3]==v2[3]:
    print("client 4 is innocent")
else:
    print("client 4 is not innocent")
