import socket
import pickle
import time
ss1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "127.0.0.1"
port = 9994
ss1.bind((ip, port))

msg1 = input("please enter value for client1:")
port1 = 9991
ss1.sendto(msg1.encode().strip(), (ip, port1))

msg2 = input("please enter value for client2:")
port2 = 9992
ss1.sendto(msg2.encode().strip(), (ip, port2))

msg3 = input("please enter value for client3:")
port3 = 9993
ss1.sendto(msg3.encode().strip(), (ip, port3))

c = 0
valueArr = [0,0,0,0]
while True:
    data, rip = ss1.recvfrom(1024)
    v = data.decode()
    if data:
        c = c + 1
        print("recv from", rip)
        if rip[1] == 9991:
            valueArr[0] = v
        if rip[1] == 9992:
            valueArr[1] = v
        if rip[1] == 9993:
            valueArr[2] = v
    if c == 3:
        break
print("my array:", valueArr)
time.sleep(5)

sdata=pickle.dumps(valueArr)
ss1.sendto(sdata, (ip, port1))
ss1.sendto(sdata, (ip, port2))
ss1.sendto(sdata, (ip, port3))

v1=v2=v3=[]
c=0
while True:
    data, rip = ss1.recvfrom(1024)
    v=pickle.loads(data)
    if data:
        c = c + 1
        print("recv from ", rip)
        if rip[1] == 9991:
            v1 = v
        if rip[1] == 9992:
            v2 = v
        if rip[1] == 9993:
            v3 = v

    if c == 3:
        break

print("all arrays ",v1," ", v2, " ",v3)

if valueArr[0]==v2[0]==v3[0]:
    print("client 1 is innocent")
else:
    print("client 1 is not innocent")

if valueArr[1]==v1[1]==v3[1]:
    print("client 2 is innocent")
else:
    print("client 2 is not innocent")

if valueArr[2]==v1[2]==v2[2]:
    print("client 3 is innocent")
else:
    print("client 3 is not innocent")
