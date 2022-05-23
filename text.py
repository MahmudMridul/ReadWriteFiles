text_file = 'text_file.txt'
reading_mode = 'r'
writing_mode = 'w'
appending_mode = 'a'
newline = '\n'
lines = ['first line', 'quick brown fox', 'did not jump', 'a lazy dog is not lazy', 'what are these']

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
    
def overwrite_with_singleline(filedir, lines):
    file = open(filedir, writing_mode)
    file.writelines(lines) #takes list of string and writes in single line
    file.close()

def overwrite_with_multiline(filedir, lines):
    file = open(filedir, writing_mode)
    for line in lines:
        line += newline
        file.write(line) #takes one string and writes
    file.close()


def append_in_singleline(filedir, lines):
    file = open(filedir, appending_mode)
    file.writelines(lines) #takes list of string and writes in single line
    file.close()

def append_in_multiline(filedir, lines):
    file = open(filedir, appending_mode)
    for line in lines:
        line += newline
        file.write(line) #takes one string and writes
    file.close()

append_in_multiline(text_file, lines)
read_file(text_file)
    
