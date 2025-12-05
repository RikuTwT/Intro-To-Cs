# James Nickell

# Period 7

# File I/O practice

# 2:23 - 2:51

file = open("Myfile.txt",'w')
content = str(input("Write a word: "))
content2 = str(input("Another word: "))
content3 = str(input("Third one: "))
file.write(content+'\n')
file.write(content2+'\n')
file.write(content3+'\n')
file.close

file = open('Myfile.txt','r')
file_line_1 = (file.readline().rstrip('\n'))
file_line_2 = (file.readline().rstrip('\n'))
file_line_3 = (file.readline().rstrip('\n'))
print(file_line_1)
print(file_line_2)
print(file_line_3) 
file.close