# try:
#     stream = open('animals.txt')
#     print(stream.read())
#     stream.close()
# except Exception as e:
#     print("An error occured: ", e)
########################################
# try:
#     stream = open('animals.txt')
#     print(stream.read(10))
#     print(stream.read(10))
#     stream.close()
# except Exception as e:
#     print("An error occured: ", e)
#########################################
# try:
#     stream = open('animals.txt')
#     counter = 0
#     character = stream.read(1)
#     while character != '':
#         counter += 1
#         print(character, end='-')
#         character = stream.read(1)
#     stream.close()
#     print('\nnumber of characters: ', counter)
# except Exception as e:
#     print("An error occured: ", e)
#############################################

# try:
#     stream = open('animals.txt')
#     counter = 0
#     line = stream.readline()
#     while line != '':
#         counter += 1
#         print(line, end='-')
#         line = stream.readline()
#     stream.close()
#     print('\nnumber of lines: ', counter)
# except Exception as e:
#     print("An error occured: ", e)

#############################################
#
# try:
#     stream = open('animals.txt')
#     lines = stream.readlines()
#     print('Content is',lines)
#     print(f"Number of lines is {len(lines)}")
#     for l in lines:
#         print(l, end='')
#     stream.close()
# except Exception as e:
#     print("An error occured: ", e)

#############################################
# 2byte 2 byte
# try:
#     stream = open('animals.txt')
#     lines = stream.readlines(2)
#     while len(lines) != 0:
#         for l in lines:
#             print(l, end='')
#         print('\n')
#         lines = stream.readlines(2)
#     stream.close()
# except Exception as e:
#     print("An error occured: ", e)

#############################################

# try:
#     stream = open('animals.txt')
#     for line in stream:
#         print(line, end='-')
# except Exception as e:
#     print("An error occured: ", e)

#############################################

# try:
#     stream = open('newFile.txt', 'w')
#     stream.write('Biliyorum ki önemli olan sıradaki dersi tam olarak öğrenmenk. \n')
#     stream.write('Diğer meseleler buna ya araç ya da mutluluk verici çeşniler.')
#     stream.close()
# except Exception as e:
#     print("An error occured.")

#############################################
#
# def show_occurences(file_name, word):
#     try:
#         stream = open(file_name)
#         lines = stream.readlines()
#         # print(lines)
#         filtered = list(filter(lambda a: word in a, lines))
#         stream.close()
#         return filtered
#     except Exception as e:
#         print("An error occured", e)
#
# filtered = show_occurences('newFile.txt','ders')
# print(filtered)
#############################################
def show_occurences(file_name, word):
    try:
        stream = open(file_name)
        num = 0
        line = stream.readline()
        while line != '':
            words = line.split(' ')
            for w in words:
                if w.lower() == word.lower():
                    num += 1
            line = stream.readline()

        stream.close()
        return num
    except Exception as e:
        print("An error occured", e)


#############################################
def count_occurences(file_name, word):
    try:
        stream = open(file_name)
        num = 0
        for line in stream:
            words = line.split(' ')
            for w in words:
                w= w.strip()
                w = w.replace(',','')
                w = w.replace('.','')
                if w.lower() == word.lower():
                    num += 1
        return num
    except Exception as e:
        print("An error occured", e)
    finally:
        stream.close()


aa = count_occurences('first_text_file.txt', 'a')
print(aa)