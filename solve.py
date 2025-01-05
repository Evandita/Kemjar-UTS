from cryptography.fernet import Fernet

with open("./output.raw", "rb") as data:
    k_declaration = data.read(1)
    if k_declaration != b"k":
        print("Invalid data")
        exit()
        
    key_len = data.read(8)
    key = data.read(int.from_bytes(key_len, "big")).decode()

    f = Fernet(key)
    
    while True:
        cmd = data.read(1)
        if cmd == b"f":
            file_len = data.read(8)
            file_name = data.read(int.from_bytes(file_len,"big")).decode()
            cipher_len = data.read(128)
            cipher = data.read(int.from_bytes(cipher_len, "big"))

            with open("./files" + file_name, "wb") as fw:
                fw.write(f.decrypt(cipher))
            print("Decrypted file:", file_name)
        else:
            break