"""Strings are immutable"""
# filename = "1.file1.txt"
# filename = "1- file1.txt"
# print(filename)
# print(filename[1])
# #filename[1] = "*" # strings are immutable
# filename = filename.replace('-','*')
# print(filename)
#
# filenames = ['1.st file', '2nd. file', '3rd file']
# filenames[0] = "-"
# #
# print(filenames)
#
# # tuple is immutable version of a list

################################################################
"""Enumerate a list"""
# a = enumerate(['x','y','z'])
# # print(a)
# # print(list(a))
#
# b = list(a)
# print(b)
# b.pop(1)
# print(b)

################################################################
"""zip example"""
# a = [1, 2, 3]
# b = [10, 20 ,30]
# x = zip(a, b)
# print(list(x))

################################################################
# contents = ["All carrots are to be sliced longitudinally",
#             "The carrots were reportedly sliced.",
#             "The slicing process was well presented."]
# filenames = ["doc.txt", "report.txt", "presentation.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../pcap/misc/files/{filename}","w")
#     file.write(content)
#     file.close()
################################################################
# txt = "I am a " \
#        "string on " \
#        "my own"
# print(txt)
################################################################
# filenames = ['a.txt', 'b.txt', 'c.txt']
# for f in filenames:
#        file = open(f"files/{f}", 'r')
#        print(file.read())
#        file.close()

