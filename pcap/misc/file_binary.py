# data = bytearray(100)
# data[0] = 100
# data[1] = 120
#
# try:
#     stream = open("file.bin", "wb")
#     stream.write(data)
#     stream.close()
# except Exception as e:
#     print("An error occured", e)
############################################
try:
    bf = open('file.bin', 'rb')
    # byte_array = bf.read()
    # read 10 bytes of the file
    byte_array = bf.read(10)
    bf.close()
except Exception as e:
    print("An error occured:", e)
############################################
# byte_array = bytearray(10)
# try:
#     bf = open('file.bin', 'rb')
#     bf.readinto(byte_array)
#     bf.close()
# except Exception as e:
#     print("An error occured:", e)

############################################

print(byte_array)

for byte in byte_array:
    print(int(byte), end=' ')

print("\n")

for byte in byte_array:
    print(hex(byte), end=' - ')

print("\n")

for byte in byte_array:
    print(bin(byte), end=' - ')




