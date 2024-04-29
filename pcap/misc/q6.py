L=["ABC\n" for x in range(10)]
f = open("myfileq6.txt","w+")
f.writelines(L)
# f.seek(0)
print(f.read())
f.close()

#The first line of the code will create a list L containing 10 elements - each element being the string "ABC\n".
#The file myfile.txt  is being open in mode "w+" which means write and update. In this mode, the file associated
#with the stream doesn't need to exist; if it doesn't exist, it will be created; both read and write operations are allowed for the stream.

#The writelines() method writes the items of a list to a file.
#So, the first three lines of the above code will work correctly (no exception is raised) : the content of the list L will be printed to the file.
#The 4th line of the code will print the content of the file to the screen but starting at the current file position (end of the file at this point) and so no visible character will be printed out.
#So, the correct answer is :The code will not raise an exception but will not print any visible characters.
#To allow the whole content of the file to be printed to the screen correctly, the file position should have been reset to the beginning of the file -
#this can be done using the method seek() which allows to move the stream reader to a particular location in the stream.
#In the above code adding f.seek(0) prior to the line print(f.read()) would have printed all 11 lines of the file to the screen.

#######################################################################################3

g = open("myfileq6_2.txt", "at")
for i in range(1,11):
    g.write('Line #' + str(i) + '\n')
g.seek(0)
print(g.readline(10))
g.close()

#In the append mode, the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created;
#if it exists the previous content of the file remains untouched and any data written to the file will be inserted at the end, after the existing data.
#Also, in this mode, the file cannot be read - it is only open for writing.


#So, the correct answer is : The code will raise an unhandled exception.

#If the file had been opened in the Append and Read mode ('a+'),
#then the code would have been executed correctly
#and the first 10 bytes of the first line of the file myfile.txt  would have been printed out
#(as a reminder the readline() method returns one line from the file;
#the optional parameter specifies the number of bytes from the line to return (default -1, which means the whole line)).


#######################################################################################3

import errno

try:
    data = open("myfile.txt", "x")
    data.write("123")
    data.close()
except IOError as e:
    if e.errno == errno.ENOENT:
        print("A")
    elif e.errno == errno.EEXIST:
        print("B")
    else:
        print("C")
else:
    print("D")

# The IOError exception object is equipped with a property named errno.
# The value of the errno property can be compared with one of the predefined symbolic constants defined in the errno module.
# The most common ones are:
# errno.ENOENT : No such file or directory
# errno.EACCES : permission denied
# errno.EEXIST : file already exists



#In the above question, myfile.txt is being opened with the x mode.
#With the x mode, the file will be opened for exclusive creation : The file must not exist before open  and  the file will be created after open.
#If if the file already exists when opening it with the x mode, then an exception FileExistsError will be raised.
#This exception is equivalent to an IOError  exception with errno value equal to errno.EEXIST .

#######################################################################################3

