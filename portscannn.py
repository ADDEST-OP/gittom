import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Skriv in ip: ")

def portscanner(port):
    try:
        connect = s.connect((target,port))
        return True
    except:
        return False

start_port = int(input("Början: "))
end_port = int(input("Sluten: "))
for ports in range(start_port, end_port):
    #print(ports)
    if portscanner(ports):
        print("Port ", ports ,"är öppen")
    else:
        print("Port ", ports, "är stängd")

