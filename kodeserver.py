import socket
import platform

IP = 'localhost'
PORT = 50001
panjang = 0
lebar = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)
print(f"Server Praktikum 10 siap di {IP}:{PORT}...")

while True:
    try:
        komm, addr = s.accept()
        print(f"Menerima koneksi dari: {addr}")

        while True:
            data = komm.recv(1024).decode()
            if not data:
                break

            print(f"Pesan Masuk: {data}")
            perintah = data.lower().strip()
            respon = "Perintah tidak valid."

            # KEGIATAN 1: DATA DIRI
            if perintah == 'nama':
                respon = "Nama: [Muhammad Nur Faiz]"
            elif perintah == 'nim':
                respon = "NIM: [L200250202]"
            elif perintah == "angkatan":
                respon = "Angkatan: [2025]"
                
            # KEGIATAN 2: INFORMASI SISTEM
            elif perintah == 'system':
                respon = f"Sistem Operasi: {platform.system()}"
            elif perintah == 'machine':
                respon = f"Mesin: {platform.machine()}"
            elif perintah == 'release':
                respon = f"Rilis OS: {platform.release()}"
            elif perintah == 'node':
                respon = f"Nama Node: {platform.node()}"
            
            # KEGIATAN 3: MENGHITUNG LUAS SEGILIMA (Segiempat NIM 2)
            elif 'parameter 1' in perintah:
                bagian = perintah.split('=') 
                if len(bagian) == 2:
                    panjang 
                    panjang = int(bagian[1].strip())
                    respon = f"Panjang ({panjang}) dicatat."
                else:
                    respon = "Format salah. Gunakan: parameter 1 = angka"

            elif 'parameter 2' in perintah:
                bagian = perintah.split('=')
                if len(bagian) == 2:
                    lebar
                    lebar = int(bagian[1].strip())
                    respon = f"Lebar ({lebar}) dicatat."
                else:
                    respon = "Format salah. Gunakan: parameter 2 = angka"

            elif perintah == 'hitung':
                luas = panjang * lebar
                respon = f"Luas Segiempat (p={panjang}, l={lebar}) adalah {luas}"

            # PERINTAH KELUAR
            elif perintah == 'keluar':
                respon = "Siap, koneksi diputus!"
                komm.send(respon.encode())
                break
                
            else:
                respon = "Perintah tidak dikenal."

            komm.send(respon.encode())

        komm.close()
        
    except KeyboardInterrupt:
        print("\nServer dimatikan.")
        break
    except Exception as e:
        print(f"Terjadi Error: {e}")
        break
