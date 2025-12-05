# James Nickell

# Period 7

# File I/O practice

# 2:23 - 2:51
# Opens a new file, then asks you to provide the contents of said file.
file = open("Myfile.txt",'w')
content = str(input("Write a word: "))
content2 = str(input("Another word: "))
content3 = str(input("Third one: "))
file.write(content+'\n')
file.write(content2+'\n')
file.write(content3+'\n')
file.close

# Opens the file again to allow it to be printed and given to the user
file = open('Myfile.txt','r')
file_line_1 = (file.readline().rstrip('\n'))
file_line_2 = (file.readline().rstrip('\n'))
file_line_3 = (file.readline().rstrip('\n'))
print(file_line_1)
print(file_line_2)
print(file_line_3) 
file.close
