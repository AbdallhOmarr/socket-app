import socket
import pickle
from PIL import Image
HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
#HOST= "10.0.1.130"
#HOST = "10.0.1.110"

PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}")
    print("Sending model to run")
    s.send(b"run sap")
    while True:
        data = s.recv(4096)
        if not data:
            break
        data1 = pickle.loads(data)
        print(data1)
        
#abdalla

input("enter to close")