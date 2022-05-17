text_file = 'text_file.txt'
reading_mode = 'r'
writing_mode = 'w'
appending_mode = 'a'

def read_file(filedir):
    file = open(filedir, reading_mode)
    print(file.read()) # reads entire file at once
    file.close()

def read_lineby_line(filedir):
    file = open(filedir, reading_mode)
    while True:
        line = file.readline() # read one line at a time
        if not line:
            break
        else:
            print(line)
    file.seek(0) #sets pointer at the start of the file
    file.close()

def read_aslist(filedir):
    file = open(filedir)
    lines = file.readlines() # read all lines as a list
    for line in lines:
        print(line)
    file.close()
