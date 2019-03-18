# print("Hello World")

# myfile = open('myfile.txt')
# mydata = myfile.read()
# print(mydata)
# print('---')
# myfile.seek(0)
# mydata = myfile.readlines()
# print(mydata)
# print('---')
# myfile.close()

# Another way of opening a file
with open('myfile.txt') as my_new_file:
    new_content = my_new_file.readlines()
    print(new_content)
