file = open("file1.txt", "r")
read = file.readlines()
modified_list = []

# for learning purpose, you will notice in the console, that we have a list of the characters from our text file
#  well you will also notice that there is a new line character, lets remove that, for now, we do not get into
#  the details of her definition i.e what she defines as alphanumeric, but this will help us later on
for line in read:
    if line[-1] == "\n":
        modified_list.append(line[:-1])
    else:
        modified_list.append(line)

print(modified_list)

file.close()
