import socket 
import platform

IP = 'localhost'
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))

s.listen()
print(f"Server siap meunggu di {IP}:{PORT}...")

while True:
    komm, addr =s.accept()
    print(f"Menerima koneksi dari: {addr}")

    while True:
        data = komm.recv(1024).decode()
        if not data:
            break

        print(f"Pesan Masuk: {data}")

        perintah = data.lower()
        if perintah == 'nama':
            respon = "Nama Server: Jarwo"
        elif perintah =='nim':
            respon = "NIM Server: L200250202"
        elif perintah == 'machine':
            respon = f"Mesin: {platform.machine()}"
        elif perintah == 'release':
            respon = f"Rilis OS: {platform.release()}"
        elif perintah == 'system':
            respon =f"Sistem Operasi: {platform.system()}"
        elif perintah == 'version':
            respon = f"Versi: {platform.version()}"
        elif perintah == 'node':
            respon = f"Nama Node: {platform.node()}"
        elif perintah == 'keluar':  
            respon ="Siap koneksi diputus!"
            komm.send(respon.encode())
            break
        else:
            respon = "Maaf, perintah tidak dikenal."

        komm.send(respon.encode())

    komm.close()