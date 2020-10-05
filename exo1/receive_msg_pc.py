import serial

# Pour vérifier le port, aller dans "Device Manager" sur Windows et checker dans "Ports COM/LPT"
port = "COM6"
conn = serial.Serial(port, 115200)

while True:
    data = conn.readline()
    if data:
        print(data.decode().strip())