import socket

IP = 'localhost'
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Sedang mencoba menghubungi server...")

try:
    s.connect((IP, PORT))
    print("Berhasil terhubung! Ketik 'keluar' untuk stop.")

    pesan = ''
    while pesan.lower() != 'keluar':
        pesan = input("Pesan: ")

        s.send(pesan.encode())

        if pesan.lower() != 'keluar':
            jawaban = s.recv(1024).decode()
            print(f"Server Menjawab: {jawaban}")

except  ConnectionRefusedError:
    print("Gagal konek! cek server mu apakah nyala?")

finally:
    s.close()        
