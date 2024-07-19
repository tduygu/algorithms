init = bytearray(10)

for i in range(len(init)):
    init[i] = 10 + i

try:
    f = open('Stars.bin', 'wb')
    f.write(init)
    f.close()
except:
    print("I/O error occured.")


data = bytearray(10)
for b in data:
    print(hex(b), end=' ')

print('\n')

try:
    f = open('Stars.bin', 'rb')
    f.readinto(data)
    f.close()
except:
    print("I/O error occured.")


for b in data:
    print(hex(b), end=' ')