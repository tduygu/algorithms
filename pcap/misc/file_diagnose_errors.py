from os import strerror

try:
    stream = open('nonexistent.file')
    stream.close()
except Exception as x:
    print(f"Error occured: {x} Error no: {x.errno}")
    print(strerror(x.errno))

